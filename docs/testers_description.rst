Keepcool Testers
================

You can find below a short description of every tester available in django-keepcool.

.. _testers_viewtester

``keepcool.testers.ViewTester``
-------------------------------

`Django View tester <https://docs.djangoproject.com/en/dev/ref/class-based-views/base/>`_. Checks whether your view is accessible and responds correctly. It checks if HttpResponse status code is the expected one.


.. _testers_createviewtester

``keepcool.testers.CreateViewTester``
-------------------------------------

`Django CreateView tester <https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/#createview>`_. Checks that :
 * the view is accessible.
 * the form submission is correctly handled.
 * a new object is created.


.. _testers_updateviewtester

``keepcool.testers.UpdateViewTester``
-------------------------------------

`Django UpdateView tester <https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/#updateview>`_. Checks that :
 * the view is accessible.
 * the form submission is correctly handled.
 * no objects are created or deleted.

.. _testers_deleteviewtester

``keepcool.testers.DeleteViewTester``
-------------------------------------

`Django DeleteView tester <https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/#deleteview>`_. Checks that :
 * the view is accessible.
 * the form submission is correctly handled.
 * an object is deleted.

.. _testers_namedformwizardtester

``keepcool.testers.NamedFormwizardTester``
------------------------------------------

`Django NamedUrlWizardView tester <http://django-formtools.readthedocs.org/en/latest/wizard.html#usage-of-namedurlwizardview>`_. Checks that :
 * the formwizard is accessible.
 * very steps are accessible and correctly chained.
 * every form submission is correctly handled.
 * an object is deleted.
