class RoleException(Exception):
    def __init__(self, msg, *args, **kwargs):
        super(RoleException, self).__init__(msg, *args, **kwargs)
