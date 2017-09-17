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
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # Instance must have an attribute named `owner`.
        return (request.method in SAFE_METHODS) or (profile.user == request.user)