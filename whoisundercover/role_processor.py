import random

from whoisundercover.role import CIVILIAN, WHITEBOARD, UNDERCOVER
from whoisundercover.undercover_exception import UndercoverException


class RoleProcessor(object):
    INVALID_UNDERCOVER_NUMBER = 'The number of undercover must be less than the half of total number'

    def __init__(self, total_num, undercover_num):
        super(RoleProcessor, self).__init__()
        if undercover_num > (total_num / 2):
            raise UndercoverException(msg=self.INVALID_UNDERCOVER_NUMBER)

        self.total_num = total_num
        self.undercover_num = undercover_num

    def assign_role_to_player(self):
        role_list = [CIVILIAN] * self.total_num

        whiteboard, undercovers = self._generate_whiteboard_and_undercover()
        role_list[whiteboard] = WHITEBOARD
        for i in undercovers:
            role_list[i] = UNDERCOVER

        return role_list

    def _generate_whiteboard_and_undercover(self):
        players = range(self.total_num)
        uc_and_wb = [players.pop(random.randint(0, len(players) - 1)) for _ in range(self.undercover_num + 1)]

        return uc_and_wb.pop(-1), uc_and_wb
