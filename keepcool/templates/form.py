from django.conf import settings

from keepcool.testers import FormTester

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class FormData(object):

    form_data = {
        "products": {
            "purchase_wizard_view-current_step": "products"
        },
        "configuration": {
            "purchase_wizard_view-current_step": "configuration",
            "configuration-MAX_NUM_FORMS": "1000",
            "configuration-MIN_NUM_FORMS": "0",
            "configuration-INITIAL_FORMS": "1",
            "configuration-TOTAL_FORMS": "1"
        },
        "discount": {
            "purchase_wizard_view-current_step": "discount"
        },
        "summary": {
            "summary-validate": "True",
            "purchase_wizard_view-current_step": "summary"
        },
    }


class FormwizardViewTestExample(FormData, FormTester):

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
