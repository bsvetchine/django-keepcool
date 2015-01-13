from .views.base import ViewTester
from .views.edit import CreateViewTester, UpdateViewTester, DeleteViewTester

from .formwizards.namedformwizards import NamedFormwizardTester


__all__ = [
    "ViewTester",
    "CreateViewTester",
    "UpdateViewTester",
    "DeleteViewTester",

    "NamedFormwizardTester"
]
