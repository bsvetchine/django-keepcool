"""
Generic django class edit view testing class util.
"""
from django.core.urlresolvers import reverse

from .._base import BaseTester


class CreateViewTester(BaseTester):

    """Generic Django CreateView tester."""

    def test_view(self):
        model = self.get_model_type(self.model).model_class()
        for user in self.get_users():
            self.log_user_in(user)
            for args in self.get_args(user):
                initial_count = model.objects.count()
                url = reverse(self.url_name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                response = self.client.post(url, self.form_data)
                self.assertTrue(response.status_code in [200, 302])
                self.assertEqual(model.objects.count(), initial_count+1)


class UpdateViewTester(BaseTester):

    """Generic Django UpdateView tester."""

    def test_view(self):
        model = self.get_model_type(self.model).model_class()
        for user in self.get_users():
            self.log_user_in(user)
            for args in self.get_args(user):
                initial_count = model.objects.count()
                url = reverse(self.url_name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                response = self.client.post(url, self.form_data)
                self.assertTrue(response.status_code in [200, 302])
                self.assertEqual(model.objects.count(), initial_count)


class DeleteViewTester(BaseTester):

    """Generic Django DeleteView tester."""

    def test_view(self):
        model = self.get_model_type(self.model).model_class()
        for user in self.get_users():
            self.log_user_in(user)
            for args in self.get_args(user):
                initial_count = model.objects.count()
                url = reverse(self.url_name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                response = self.client.post(url, self.form_data)
                self.assertTrue(response.status_code in [200, 302])
                self.assertEqual(model.objects.count(), initial_count-1)
