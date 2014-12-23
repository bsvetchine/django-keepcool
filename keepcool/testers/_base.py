from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class BaseTester(object):

    def get_users_by_permission(self):
        """List all users that have access permission."""
        app_label, codename = self.permission_required.split(".")
        perm = Permission.objects.get(
            content_type__app_label=app_label, codename=codename)
        return User.objects.filter(
            Q(groups__permissions=perm) | Q(user_permissions=perm)
        ).distinct()

    def get_users_by_group(self):
        """List all users from each group."""
        group_required = self.group_required
        if type(self.group_required) in (str, unicode):
            group_required = [group_required]
        return User.objects.filter(
            groups__in=group_required).distinct()

    def get_users(self):
        """List all users that have access to view."""
        if hasattr(self, "permission_required"):
            return self.get_users_by_permission()
        elif hasattr(self, "group_required"):
            return self.get_users_by_group()
        return User.objects.all()

    def get_args(self, user):
        """Returns a list containing all args for reversing url name."""
        args = []
        if not hasattr(self, "get_first_args"):
            args.append([])
        else:
            for first_arg in self.get_first_args(user):
                if not hasattr(self, "get_second_args"):
                    args.append([first_arg.pk])
                else:
                    for second_arg in self.get_second_args(user, first_arg):
                        if not hasattr(self, "get_third_args"):
                            args.append([first_arg.pk, second_arg.pk])
                        else:
                            for third_arg in self.get_third_args(user,
                                                                 first_arg,
                                                                 second_arg):
                                args.append([
                                    first_arg.pk, second_arg.pk, third_arg.pk])
        return args
