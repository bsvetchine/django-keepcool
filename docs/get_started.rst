Examples
========

Django-keepcool : get started !


.. _examples_basic

``static_page``
---------------
::

        from django.test import TestCase
        from keepcool.testers import ViewTester


        class HomeViewTest(ViewTester, TestCase):

            url_name = "home"
            expected_status_code = 200


.. _examples_dynamic

``dynamic page``
---------------

::

        from django.test import TestCase
        from keepcool.testers import ViewTester


        class DashboardViewTest(ViewTester, TestCase):

            url_name = "dashboard"
            expected_status_code = 200

            def setUp(self):
                # fill testing data here
                pass


.. _examples_create

``create view testing``
-----------------------

::

        from django.contrib.auth import get_user_model
        from django.test import TestCase
        from keepcool.testers import CreateViewTester


        class ProfileCreateViewTest(CreateViewTester, TestCase):

            url_name = "profile_create"
            expected_status_code = 200
            form_data = {
                "email": "data@example.com",
                "first_name": "Jean",
                "last_name": "Reinhardt",
            }

            def get_users(self):
                """List all users that have access to view."""
                return get_user_model.objects.filter(groups__in=["administrator"])

            def setUp(self):
                # fill testing data here
                pass

            def log_user_in(self, user):
                """Log in user in argument."""
                user.set_password("pass")
                self.client.login(username=user.email, password="pass")


.. _examples_formwizardview

``formwizard view testing``
---------------------------

::

        from django.test import TestCase
        from keepcool.testers import NamedFormwizardTester


        class KeepcoolBase(object):

            def log_user_in(self, user):
                """Log in user in argument."""
                user.set_password("pass")
                self.client.login(username=user.email, password="pass")

            def setUp(self):
                # fill testing data here
                pass


        class PurchaseWizardData(object):

            """
            PurchaseWizard testing data.

            PurchaseWizardData defines a set of data to be used in
            testing with the NamedFormwizardTester class."""

            wizard_url_name = "client_buy"
            wizard_url_step_name = "client_buy_step"
            wizard_done_step_name = "buy_done"
            wizard_steps = ["products", "configuration", "discount"]
            wizard_form_data = {
                "products": {
                    # all your product form data.
                    "client_purchase_wizard_view-current_step": "products"
                },
                "configuration": {
                    # all your configuration form data.
                    "client_purchase_wizard_view-current_step": "configuration",
                },
                "discount": {
                    # all your summary form data.
                    "client_purchase_wizard_view-current_step": "discount"
                },
            }


        class PurchaseWizardViewTest(PurchaseWizardData, NamedFormwizardTester,
                                     KeepcoolBase, TestCase):

            url_name = "client_buy"
            expected_status_code = 200


.. _examples_permissionview

``braces access restricted view``
--------------------------------------

* group_required protection

::

    class ViewTest(
            #...,
            TestCase):

        # ...
        group_required = ["administrators", ]


* permission_required production

::

    class ViewTest(
            #...,
            TestCase):

        # ...
        permission_required = "app_name.perm_name"