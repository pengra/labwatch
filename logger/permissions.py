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
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return session.student.school == request.user.profile.school
            return session.student.school == request.user.profile.school and (request.user.profile.librarian or request.user.profile.engineer)
        return False


class KioskPermission(BasePermission):
    """
    Allow librarians to create and modify kiosks.
    """

    def has_object_permission(self, request, view, kiosk):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return kiosk.school == request.user.profile.school
            return kiosk.school == request.user.profile.school and (request.user.profile.librarian)
        return False


class ImageCardPermission(BasePermission):
    """
    Allow librarians to modify image cards. Allow anyone to see them.
    """

    def has_object_permission(self, request, view, card):
        return (
            request.user.is_authenticated and 
            request.method in SAFE_METHODS or 
            (card.school == request.user.profile.school and request.user.profile.librarian)
        )