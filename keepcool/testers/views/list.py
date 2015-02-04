"""
Generic django class list view testing class util.
"""
from django.core.urlresolvers import reverse

from .._base import BaseTester


class ListViewTester(BaseTester):

    """Generic Django FormView tester."""

    def process(self, user=None):
        for args in self._get_args(user=user):
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, self.expected_status_code)
