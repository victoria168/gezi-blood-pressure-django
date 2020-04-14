from rest_framework import permissions


class RecordPermission(permissions.BasePermission):
    """
    Restricts Charts APIs depending on the UserAccess
    """
    message = 'You don\'t have permission to perform this operation on ' + \
        'this Chart.'

    def has_permission(self, request, view):

        print(request.user)
        return True
