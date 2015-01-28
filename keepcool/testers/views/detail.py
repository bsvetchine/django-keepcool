"""
Generic django detail view testing class util.
"""
from django.core.urlresolvers import reverse

from .._base import BaseTester


class DetailViewTester(BaseTester):

    """Generic Django DetailView tester."""

    def process(self, user=None):
        for args in self._get_args(user=user):
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            while response.status_code in [301, 302]:
                response = self.client.get(response.url)
            self.assertEqual(response.status_code, 200)
