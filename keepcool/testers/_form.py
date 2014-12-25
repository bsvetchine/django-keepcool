"""Generic form testing class util."""
from django.core.urlresolvers import reverse

from ._base import BaseTester


class FormTester(BaseTester):

    def test_form(self):
        for user in self.get_users():
            self.log_user_in(user)
            for args in self.get_args(user):
                url = reverse(self.url_name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                response = self.client.post(url, self.form_data)
                self.assertEqual(response.status_code, 200)
