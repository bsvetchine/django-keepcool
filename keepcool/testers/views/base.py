"""
Generic django class base view testing class util.
"""
from django.core.urlresolvers import reverse

from .._base import BaseTester


class ViewTester(BaseTester):

    """Generic Django BaseView tester."""

    def test_url_access(self):
        for user in self.get_users():
            self.log_user_in(user)
            for args in self.get_args(user):
                url = reverse(self.url_name, args=args)
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code, self.expected_status_code)
