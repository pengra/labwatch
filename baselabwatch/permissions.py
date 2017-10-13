"""
Common useful functions/classes regarding permissions
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS

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
        "Allow only the school librarians view "
        return student.school == request.user.profile.school