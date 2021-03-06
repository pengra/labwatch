import json
from django.db import IntegrityError
from django.views.generic import View
from django.shortcuts import HttpResponse
from defusedxml.ElementTree import parse
from labwatch.settings import MAXUPLOADSIZE
from baselabwatch.forms import XMLFileUploadForm
from baselabwatch.models import Student


class XMLUploadView(View):

    def post(self, request):

        if not request.user.is_authenticated():
            response = HttpResponse(json.dumps(
                {"errors": ["Not authenticated"]}), content_type='application/json')
            response.status_code = 403
            return response

        if not request.user.profile.school:
            response = HttpResponse(json.dumps(
                {"errors": ["Not associated with any school"]}), content_type='application/json')
            response.status_code = 403
            return response

        # FOR DEBUGGING FRONT END
        # import time; time.sleep(5);

        xmlform = XMLFileUploadForm(request.POST, request.FILES)
        if xmlform.is_valid() and xmlform.cleaned_data['spreadsheet'].size < MAXUPLOADSIZE:
            dupes = 0
            new_students = 0
            fails = 0
            overwrite_dupes = xmlform.cleaned_data['dupe_action'] == 'overwrite'

            spreadsheet = xmlform.cleaned_data['spreadsheet']
            content = parse(spreadsheet)
            root = content.getroot()

            for row in root:
                student_data = {
                    'school': request.user.profile.school
                }
                failed = False
                for data in row:
                    try:
                        if data.tag == xmlform.cleaned_data['studentid'] and len(data.text) > 0:
                            student_data['student_id'] = data.text
                        elif data.tag == xmlform.cleaned_data['fname'] and len(data.text) > 0:
                            student_data['first_name'] = (data.text)
                        elif data.tag == xmlform.cleaned_data['lname'] and len(data.text) > 0:
                            student_data['last_name'] = (data.text)
                        elif data.tag == xmlform.cleaned_data['grade'] and len(data.text) > 0:
                            student_data['grade'] = data.text
                        elif data.tag == xmlform.cleaned_data['teacher'] and len(data.text) > 0:
                            student_data['teacher'] = (data.text)
                        elif len(xmlform.cleaned_data['nickname']) and data.tag == xmlform.cleaned_data['nickname'] and len(data.text) > 0:
                            student_data['nick_name'] = data.text
                        elif len(xmlform.cleaned_data['email']) and data.tag == xmlform.cleaned_data['email'] and len(data.text) > 0:
                            student_data['email'] = data.text
                    except KeyError:
                        fails += 1
                        failed = True

                if failed:
                    continue

                student = Student(**student_data)
                try:
                    student.save()
                    new_students += 1
                except IntegrityError:
                    if overwrite_dupes:
                        try:
                            old_student = Student.objects.get(
                                student_id=student_data['student_id'])
                            old_student.delete()
                            student.save()
                            dupes += 1
                        except (ValueError, KeyError):
                            fails += 1
                    else:
                        dupes += 1
                except ValueError:
                    fails += 1

            response = HttpResponse(json.dumps({
                'new': new_students,
                'dupes': dupes,
                'fails': fails,
                'overwrite': overwrite_dupes
            }), content_type='application/json')
            response.status_code = 201
        else:
            response = HttpResponse(json.dumps(
                xmlform.errors), content_type='application/json')
            response.status_code = 400

        return response
