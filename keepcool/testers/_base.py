from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core import management

if "south" in settings.INSTALLED_APPS:
    from south.models import MigrationHistory

from .. import app_settings


class BaseTester(object):

    def reset_user_password(self):
        get_user_model().objects.all().set_password(
            app_settings.KEEPCOOL_GENERIC_PASSWORD)

    def delete_db_initial_content(self):
        Site.objects.all().delete()
        ContentType.objects.all().delete()
        Permission.objects.all().delete()
        get_user_model().objects.all().delete()
        if "south" in settings.INSTALLED_APPS:
            MigrationHistory.objects.all().delete()

    def setUp(self):
        #management.call_command("dumpdefaultdata")
        self.delete_db_initial_content()
        print "Successfully deleted database initial content"
        management.call_command("loaddefaultdata")
        print "Sucessfully loaded data form the dump."
        self.reset_user_password()
        print "Sucessfully reset all user passwords"
        super(BaseTester, self).setUp()

    def get_args(self, user):
        args = []
        if not hasattr(self, "get_first_args"):
            args.append([])
        else:
            for first_arg in self.get_first_args(user):
                if not hasattr(self, "get_second_args"):
                    args.append([first_arg])
                else:
                    for second_arg in self.get_second_args(user, first_arg):
                        if not hasattr(self, "get_third_args"):
                            args.append([first_arg, second_arg])
                        else:
                            for third_arg in self.get_third_args(user,
                                                                 first_arg,
                                                                 second_arg):
                                args.append([first_arg, second_arg, third_arg])
        return args
