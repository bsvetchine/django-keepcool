import copy
import lxml.html

from django.conf import settings

from keepcool.testers import FormwizardTester

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class FormwizardData(object):

    wizard_url_name = "client_buy"
    wizard_url_step_name = "client_buy_step"
    wizard_done_step_name = "buy_done"
    wizard_steps = ["products", "configuration", "discount", "summary"]
    wizard_form_data = {
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

    def get_products(self, response):
        """Select the first center in the select field."""
        response = self.client.get(response.url)
        html = lxml.html.fromstring(str(response))
        product_names = html.xpath(
            ".//div[@class='product-in-list']//input/@name")
        return {product_names[0]: 1}

    def get_form_data(self, form_name, response):
        """Set fields value that can't be set in a static way.

        This function sets values according to runtime data available.
        """
        form_data = copy.deepcopy(self.wizard_form_data[form_name])
        if form_name == "products":
            form_data.update(self.get_products(response))
        return form_data


class FormwizardViewTestExample(FormwizardData, FormwizardTester):

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
