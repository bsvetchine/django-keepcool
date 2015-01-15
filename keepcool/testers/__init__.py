from .views.base import ViewTester, RedirectViewTester
from .views.edit import (
    FormViewTester, CreateViewTester, UpdateViewTester, DeleteViewTester)

from .formwizards.namedformwizards import NamedFormwizardTester


__all__ = [
    "ViewTester",
    "RedirectViewTester",

    "FormViewTester",
    "CreateViewTester",
    "UpdateViewTester",
    "DeleteViewTester",

    "NamedFormwizardTester"
]
