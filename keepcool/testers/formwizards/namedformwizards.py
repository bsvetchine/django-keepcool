"""
Generic namedformwizard testing class util.
"""
from django.core.urlresolvers import reverse

from .._base import BaseTester


class NamedFormwizardTester(BaseTester):

    """Generic NamedFormwizard tester."""

    def get_form_data(self, step, response):
        """
        Get form data located in wizard_form_data dictionnary.

        This method may be overriden by to be able to set dynamic data.
        """
        return self.wizard_form_data[step]

    def get_wizard_url(self, step=None):
        """
        Return url.

        If formwizard url need a special url args, you need to specify
        it in self.wizard_url_args.
        """
        if hasattr(self, "wizard_url_args"):
            args = getattr(self, "wizard_url_args")
        else:
            args = []
        if not step:
            url_name = self.wizard_url_name
        else:
            url_name = self.wizard_url_step_name
            args += [step]
        return reverse(url_name, args=args)

    def process(self, user=None):
        for args in self._get_args(user):
            url = reverse(self.url_name, args=args)
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
                current_step = wizard_context["steps"].current
                if current_step != step and step in self.optional_steps:
                    continue
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
