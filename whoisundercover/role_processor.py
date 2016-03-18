from whoisundercover.undercover_exception import UndercoverException


class RoleProcessor(object):
    INVALID_UNDERCOVER_NUMBER = 'The number of undercover must be less than the half of total number'

    def __init__(self, total_num, undercover_num):
        super(RoleProcessor, self).__init__()
        if undercover_num > (total_num / 2):
            raise UndercoverException(msg=self.INVALID_UNDERCOVER_NUMBER)

        self.total_num = total_num
        self.undercover_num = undercover_num
