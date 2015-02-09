"""
Generic django class edit view testing class util.
"""
from django.core.urlresolvers import reverse

from .._base import BaseTester


class FormViewTester(BaseTester):

    """Generic Django FormView tester."""

    def process(self, user=None):
        for args in self._get_args(user=user):
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            while response.status_code in [301, 302]:
                response = self.client.get(response.url)
            self.assertEqual(response.status_code, 200)
            response = self._post(url, self.form_data)
            self.assertTrue(response.status_code in [200, 302])


class CreateViewTester(BaseTester):

    """Generic Django CreateView tester."""

    def process(self, user=None):
        model = self._get_model_type(self.model).model_class()
        for args in self._get_args(user=user):
            initial_count = model.objects.count()
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            response = self._post(url, self.form_data)
            self.assertTrue(response.status_code in [200, 302])
            self.assertEqual(model.objects.count(), initial_count+1)


class UpdateViewTester(BaseTester):

    """Generic Django UpdateView tester."""

    def process(self, user=None):
        model = self._get_model_type(self.model).model_class()
        for args in self._get_args(user=user):
            initial_count = model.objects.count()
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            response = self._post(url, self.form_data)
            self.assertTrue(response.status_code in [200, 302])
            self.assertEqual(model.objects.count(), initial_count)


class DeleteViewTester(BaseTester):

    """Generic Django DeleteView tester."""

    def process(self, user=None):
        model = self._get_model_type(self.model).model_class()
        for args in self._get_args(user=user):
            initial_count = model.objects.count()
            url = reverse(self.url_name, args=args)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            response = self._post(url, self.form_data)
            self.assertTrue(response.status_code in [200, 302])
            self.assertEqual(model.objects.count(), initial_count-1)
