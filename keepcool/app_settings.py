from django.conf import settings


KEEPCOOL_GENERIC_PASSWORD = getattr(settings, "KEEPCOOL_GENERIC_PASSWORD",
                                    "One string to rule them all")
