from rest_framework.permissions import BasePermission

class IsTrainer(BasePermission):

    def has_permission(self, request, view):

        if request.user.role == "trainer":

            return True

        else:

            return False

class IsStudent(BasePermission):

    def has_permission(self, request, view):

        if request.user.role == "student":

            return True

        else:

            return False