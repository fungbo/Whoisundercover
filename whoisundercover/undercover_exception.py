

class UndercoverException(Exception):
    def __init__(self, msg, *args, **kwargs):
        super(UndercoverException, self).__init__(msg, *args, **kwargs)
