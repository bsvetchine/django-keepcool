"""Generic form testing class util."""
from django.core.urlresolvers import reverse

from ._base import BaseTester


class FormTester(BaseTester):

    """Mixin used in wizard view tests."""

    def test_form(self):
        for user in self.get_users():
            for args in self.get_args(user):
                url = reverse(self.url_name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                response = self.client.post(url, self.form_data)
                self.assertEqual(response.status_code, 200)

    def go_though_form(self):
        for user in self.get_users():
            for args in self.get_args(user):
                url = reverse(self.url_name, args=args)
                response = self.client.post(url, self.form_data)
                return self.client.get(response.url)
