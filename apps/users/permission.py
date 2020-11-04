from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        try:
            role = request.user.role
            return role == 1
        except Exception:
            return True

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        try:
            role = request.user.role
            return role == 2
        except Exception:
            return True

class IsFieldManagerUser(BasePermission):
    def has_permission(self, request, view):
        try:
            role = request.user.role
            return role == 3
        except Exception:
            return True

class IsOperatorUser(BasePermission):
    def has_permission(self, request, view):
        try:
            role = request.user.role
            return role == 3
        except Exception:
            return True
