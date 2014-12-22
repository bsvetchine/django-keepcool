from django.core.urlresolvers import reverse

from ._base import BaseTester


class ViewTester(BaseTester):

    def test_url_access(self):
        print "Start test_url_acess"
        for user in self.get_users():
            print "--------------------------"
            print "user : " + str(user.email)
            for args in self.get_args(user):
                print "   args : " + str(args)
                url = reverse(self.urlname, args=args)
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code, self.expected_status_code)
