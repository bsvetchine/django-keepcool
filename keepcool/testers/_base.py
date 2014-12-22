class BaseTester(object):

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
