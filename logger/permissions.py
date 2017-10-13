"""
Common useful functions/classes regarding permissions
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS

class SessionPermission(BasePermission):
    """
    Allow kiosks and librarians to modify logs.
    """

    def has_object_permission(self, request, view, session):
        "Only allow librarians to view/create and teachers and other associated accounts to view."
        if request.method in SAFE_METHODS:
            return session.student.school == request.user.profile.school
        return session.student.school == request.user.profile.school and (request.user.profile.librarian or request.user.profile.engineer)


