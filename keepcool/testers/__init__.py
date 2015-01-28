from .views.base import ViewTester, TemplateViewTester, RedirectViewTester
from .views.detail import DetailViewTester
from .views.edit import (
    FormViewTester, CreateViewTester, UpdateViewTester, DeleteViewTester)

from .formwizards.namedformwizards import NamedFormwizardTester


__all__ = [
    "ViewTester",
    "TemplateViewTester",
    "RedirectViewTester",

    "DetailViewTester",

    "FormViewTester",
    "CreateViewTester",
    "UpdateViewTester",
    "DeleteViewTester",

    "NamedFormwizardTester"
]
