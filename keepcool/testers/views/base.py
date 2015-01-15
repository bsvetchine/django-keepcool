"""
Generic django class base view testing class util.
"""
from django.core.urlresolvers import reverse

from .._base import BaseTester


class ViewTester(BaseTester):

    """Generic Django BaseView tester."""

    def process(self, user=None):
        for args in self._get_args(user=user):
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, self.expected_status_code)


class RedirectViewTester(BaseTester):

    """Generic Django RedirectView tester."""

    def process(self, user=None):
        for args in self._get_args(user=user):
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, 302)
            response = self.client.get(response.url)
            self.assertEqual(
                response.status_code, self.expected_status_code)


class TemplateViewTester(BaseTester):

    """Generic Django TemplateViewTester tester."""

    def process(self, user=None):
        for args in self._get_args(user=user):
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, self.expected_status_code)
