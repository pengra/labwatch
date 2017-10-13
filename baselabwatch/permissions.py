"""
Common useful functions/classes regarding permissions
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):

    def has_object_permission(self, request, view, user):
        return user == request.user


class ProfilePermission(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, profile):
        "Allow only the owner of the profile to view."
        return profile.user == request.user


class StudentPermission(BasePermission):

    def has_object_permission(self, request, view, student):
        "Allow only the school librarians view"
        return student.school == request.user.profile.school


class SchoolPermission(BasePermission):

    def has_object_permission(self, request, view, school):
        "Allow only the school primary contact edit."
        if request.method in SAFE_METHODS:
            return request.user.profile.school == school
        return school.primary_contact == request.user