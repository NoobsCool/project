from rest_framework.permissions import BasePermission


class CanView(BasePermission):

    def has_permission(self, request, view):
        pass