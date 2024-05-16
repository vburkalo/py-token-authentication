from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or (request.user and request.user.is_authenticated)
        ) or (
            request.method == "POST"
            and request.user and request.user.is_authenticated
        ) or (
            request.user and request.user.is_staff
        )