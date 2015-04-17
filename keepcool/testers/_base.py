from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db.models.base import ModelBase


User = get_user_model()


class BaseTester(object):

    anonymous = False
    ajax_post = False

    def get_users_by_permission(self):
        """List all users that have access permission."""
        permissions = []
        required = self.permission_required
        if isinstance(required, str):
            required = [required]
        for perm_required in required:
            app_label, codename = perm_required.split(".")
            perm = Permission.objects.get(
                content_type__app_label=app_label, codename=codename)
            permissions.append(perm.id)
        return User.objects.filter(
            Q(groups__permissions__id__in=permissions) |
            Q(user_permissions__id__in=permissions)
        )

    def get_users_by_group(self):
        """List all users from each group."""
        group_required = self.group_required
        if isinstance(group_required, str):
            # python3 fallback
            group_required = [group_required]
        elif isinstance(group_required, unicode):
            # python2 fallback
            group_required = [group_required]
        return User.objects.filter(
            groups__name__in=group_required)

    def get_users(self):
        """List all users that have access to view."""
        users = User.objects.all()
        if hasattr(self, "permission_required"):
            # get_users_by_permission may contains duplicate users.
            # Using intersection should eliminate duplicate elements.
            users &= self.get_users_by_permission()
        if hasattr(self, "group_required"):
            users &= self.get_users_by_group()
        return users

    def get_level1_args(self, user=None):
        """Return a list containg all args list combination."""
        return [[first_arg] for first_arg in self.get_first_args(user)]

    def get_level2_args(self, user=None):
        """Return a list containg all args list combination."""
        level2_args = []
        for first_arg in self.get_level1_args(user):
            level2_args += [
                [first_arg, second_arg] for second_arg in
                self.get_second_args(user, first_arg)
            ]
        return level2_args

    def get_level3_args(self, user=None):
        """Return a list containg all args list combination."""
        level3_args = []
        for first_arg, second_arg in self.get_level2_args(user):
            level3_args += [
                [first_arg, second_arg, third_arg] for third_arg in
                self.get_third_args(user, first_arg, second_arg)
            ]
        return level3_args

    def get_level4_args(self, user=None):
        """Return a list containg all args list combination."""
        level4_args = []
        for arg1, arg2, arg3 in self.get_level3_args(user):
            level4_args += [
                [arg1, arg2, arg3, arg4] for arg4 in
                self.get_fourth_args(user, arg1, arg2, arg3)
            ]
        return level4_args

    def get_level5_args(self, user=None):
        """Return a list containg all args list combination."""
        level5_args = []
        for arg1, arg2, arg3, arg4 in self.get_level4_args(user):
            level5_args += [
                [arg1, arg2, arg3, arg4, arg5] for arg5 in
                self.get_fitfh_args(user, arg1, arg2, arg3, arg4)
            ]
        return level5_args

    def get_view_args(self, user=None):
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

    def _get_args(self, user):
        """Get all args to reverse view by name."""
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

    def _get_model_type(self, model_descr):
        """
        Get content type object from model string.

        Model string format : 'django_app.django_model'.
        """
        app_label, model = model_descr.lower().split(".")
        return ContentType.objects.get(app_label=app_label, model=model)

    def _post(self, url, data=None):
        """
        Post data to url.

        If self.ajax_post, it will simulate an ajax post.
        """
        if self.ajax_post:
            response = self.client.post(
                url, data, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        else:
            response = self.client.post(url, data)
        return response

    def test_view(self):
        """Base unit test."""
        if self.anonymous:
            self.process()
        else:
            for user in self.get_users():
                self.log_user_in(user)
                self.process(user)
