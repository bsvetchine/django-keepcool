from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models import Q
from django.db.models.base import ModelBase


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
        if type(group_required) in (str, unicode):
            group_required = [group_required]
        return User.objects.filter(
            groups__name__in=group_required).distinct()

    def get_users(self):
        """List all users that have access to view."""
        if hasattr(self, "permission_required"):
            return self.get_users_by_permission()
        elif hasattr(self, "group_required"):
            return self.get_users_by_group()
        return User.objects.all()

    def get_level1_args(self, user):
        """Return a list containg all args list combination."""
        return [[first_arg] for first_arg in self.get_first_args(user)]

    def get_level2_args(self, user):
        """Return a list containg all args list combination."""
        level2_args = []
        for first_arg in self.get_level1_args(user):
            level2_args += [
                [first_arg, second_arg] for second_arg in
                self.get_second_args(user, first_arg)
            ]
        return level2_args

    def get_level3_args(self, user):
        """Return a list containg all args list combination."""
        level3_args = []
        for first_arg, second_arg in self.get_level2_args(user):
            level3_args += [
                [first_arg, second_arg, third_arg] for third_arg in
                self.get_third_args(user, first_arg, second_arg)
            ]
        return level3_args

    def get_level4_args(self, user):
        """Return a list containg all args list combination."""
        level4_args = []
        for arg1, arg2, arg3 in self.get_level3_args(user):
            level4_args += [
                [arg1, arg2, arg3, arg4] for arg4 in
                self.get_fourth_args(user, arg1, arg2, arg3)
            ]
        return level4_args

    def get_level5_args(self, user):
        """Return a list containg all args list combination."""
        level5_args = []
        for arg1, arg2, arg3, arg4 in self.get_level4_args(user):
            level5_args += [
                [arg1, arg2, arg3, arg4, arg5] for arg5 in
                self.get_fitfh_args(user, arg1, arg2, arg3, arg4)
            ]
        return level5_args

    def get_view_args(self, user):
        """Returns a list containing all args for reversing url name.

        Double list format ; [[first_arg, second_arg, third_arg],]."""
        if hasattr(self, "get_fitfh_args"):
            args = self.get_level5_args(user)
        elif hasattr(self, "get_fourth_args"):
            args = self.get_level4_args(user)
        elif hasattr(self, "get_third_args"):
            args = self.get_level3_args(user)
        elif hasattr(self, "get_second_args"):
            args = self.get_level2_args(user)
        elif hasattr(self, "get_first_args"):
            args = self.get_level1_args(user)
        else:
            args = []
        return args

    def get_args(self, user):
        args = []
        for view_args in self.get_view_args(user):
            combination = []
            for arg in view_args:
                if isinstance(arg.__class__, ModelBase):
                    combination.append(arg.pk)
                else:
                    combination.append(arg)
            args.append(combination)
        if not args:
            return [[]]
        return args
