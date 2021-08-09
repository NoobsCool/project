from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CanView(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True


class CanEdit(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

