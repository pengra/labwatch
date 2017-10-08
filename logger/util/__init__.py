import xlsxwriter
from pytz import timezone
from django.core.files.temp import NamedTemporaryFile
from baselabwatch.models import Student
from logger.models import StudentSession, Kiosk, PollChoice, PollQuestion


ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q',
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF'
]

# DateTimes appear as: 2017-09-28 15:49:38+00:00
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def get_last_log(student):
    "Get last StudentSession for Student."
    return StudentSession.objects.filter(student=student).last()


def export_logs(export_form_data, target_tz):
    "Create an excel table to export for the user."
    temporary_file = NamedTemporaryFile(suffix='.xlsx')

    workbook = xlsxwriter.Workbook(
        temporary_file, 
        {
            'in_memory': True, 
            'remove_timezone': True
        }
    )

    datetime_format = workbook.add_format({'num_format': "dd/mm/yy hh:mm:ss AM/PM"})

    worksheet = workbook.add_worksheet()
    column_cursor = 0

    if export_form_data.get('id_column'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'Student ID')
        column_cursor += 1
    if export_form_data.get('names'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'First Name')
        column_cursor += 1
        worksheet.write(ALPHABET[column_cursor] + '1', 'Last Name')
        column_cursor += 1
    if export_form_data.get('grade'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'Grade')
        column_cursor += 1
    if export_form_data.get('teachers'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'Teacher')
        column_cursor += 1
    if export_form_data.get('in_column'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'Time in')
        column_cursor += 1
    if export_form_data.get('in_method'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'Sign in method')
        column_cursor += 1
    if export_form_data.get('out'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'Time out')
        column_cursor += 1
    if export_form_data.get('out_method'):
        worksheet.write(ALPHABET[column_cursor] + '1', 'Sign out method')
        column_cursor += 1

    if column_cursor:
        for row_index, log in enumerate(export_form_data['target'].split(','), 2):
            column_cursor = 0
            # try:
            # DateTimes appear as: 2017-09-28 15:49:38+00:00
            session = StudentSession.objects.get(pk=log)
            if export_form_data.get('id_column'):
                worksheet.write(
                    ALPHABET[column_cursor] + str(row_index), 
                    session.student.student_id
                )
                column_cursor += 1
            if export_form_data.get('names'):
                worksheet.write(
                    ALPHABET[column_cursor] + str(row_index), session.student.first_name)
                column_cursor += 1
                worksheet.write(
                    ALPHABET[column_cursor] + str(row_index), session.student.last_name)
                column_cursor += 1
            if export_form_data.get('grade'):
                worksheet.write(
                    ALPHABET[column_cursor] + str(row_index), session.student.grade)
                column_cursor += 1
            if export_form_data.get('teachers'):
                worksheet.write(
                    ALPHABET[column_cursor] + str(row_index), session.student.teacher)
                column_cursor += 1
            if export_form_data.get('in_column'):
                
                worksheet.write_datetime(
                    ALPHABET[column_cursor] + str(row_index), 
                    session.sign_in_timestamp.astimezone(timezone(target_tz)), 
                    datetime_format
                )
                column_cursor += 1
            if export_form_data.get('in_method'):
                worksheet.write(
                    ALPHABET[column_cursor] + str(row_index), 
                    session.sign_in_mode
                )
                column_cursor += 1
            if export_form_data.get('out'):
                worksheet.write_datetime(
                    ALPHABET[column_cursor] + str(row_index), 
                    session.sign_out_timestamp.astimezone(timezone(target_tz)), 
                    datetime_format
                )
                column_cursor += 1
            if export_form_data.get('out_method'):
                worksheet.write(
                    ALPHABET[column_cursor] + str(row_index), session.sign_out_mode)
                column_cursor += 1
        
        # close the work book and set cursor to 0
        workbook.close()
        temporary_file.seek(0)

        return temporary_file

    # return none if user selected no columns
    del temporary_file
    del workbook
    del worksheet
    
def update_poll(kiosk, new_question, new_choices):
    "Directly take form data and create new objects."
    new_question = PollQuestion(question_text=new_question)
    new_question.save()
    for choice in new_choices.split('\n'):
        PollChoice(question=new_question, choice_text=choice).save()
    if kiosk.poll:
        kiosk.poll.delete()
    kiosk.poll = new_question
