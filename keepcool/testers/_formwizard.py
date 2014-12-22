"""
Generic formwizard testing class util.

You need to associate FormWizardTestingTool with a test case class
defining a set of data. The test case classes are generally set in
the tandoori client app.
"""
from django.core.urlresolvers import reverse
from django.test import TestCase

from ._base import BaseTester


class FormwizardTester(BaseTester, TestCase):

    """Mixin used in wizard view tests."""

    def get_form_data(self, step, response):
        """
        Get form data located in wizard_form_data dictionnary.

        This method may be overriden by to be able to set dynamic data.
        """
        return self.wizard_form_data[step]

    def test_formwizard(self):
        # Testing access to formwizard
        for user in self.get_users():
            for args in self.get_args(user):
                url = reverse(self.urlname, args=args)
                response = self.client.get(url)
                while not self.client.get(response.url).context:
                    response = self.client.get(response.url)
                self.assertEqual(
                    response.url,
                    "http://testserver" +
                    self.get_wizard_url(step=self.wizard_steps[0])
                )
                # Check url name configuration
                wizard = self.client.get(response.url).context['wizard']
                self.assertEqual(wizard['url_name'], self.wizard_url_step_name)
                # Check wizard forms
                for step in self.wizard_steps:
                    wizard_context = self.client.get(
                        response.url).context["wizard"]
                    self.assertEqual(wizard_context["steps"].current, step)
                    response = self.client.post(
                        response.url,
                        self.get_form_data(step, response)
                    )
                # Check wizard form done
                self.assertEqual(
                    response.url,
                    "http://testserver" +
                    self.get_wizard_url(step=self.wizard_done_step_name)
                )
                response = self.client.get(response.url)

    def go_though_formwizard(self):
        for user in self.users:
            for args in self.get_args(user):
                url = reverse(self.urlname, args=args)
                response = self.client.get(url)
                while not self.client.get(response.url).context:
                    response = self.client.get(response.url)
                for step in self.wizard_steps:
                    response = self.client.post(
                        response.url,
                        self.get_form_data(step, response)
                    )
                return self.client.get(response.url)
