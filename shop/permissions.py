from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSenderPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.profile.is_sender:
            return True


class IsSenderAndOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.profile.is_sender:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and obj.profile == request.user.profile and\
                request.user.profile.is_sender:
            return True


class IsBuyerAndOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.profile.is_sender is False:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and obj.profile == request.user.profile and \
                request.user.profile.is_sender is False:
            return True
