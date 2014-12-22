from django.conf import settings

from django_keepcool.testers import ViewTester

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ViewTestExample(ViewTester):

    url_name = "buena_view"
    expected_status_code = 200

    def get_users(self):
        """List all user that have access to this url."""
        return

    def get_first_args(self, user):
        """List all values accepted as first argument.

        Returns all values accepted as first argument for the specific user."""
        return

    def get_second_args(self, user, first_arg):
        """List all values accepted as second argument.

        Returns all values accepted as second argument given the user and first
        argument."""
        return

    def get_third_args(self, user, first_arg, second_arg):
        """List all values accepted as third argument.

        Returns all values accepted as third argument givent the user, first
        and second argument."""
        return
