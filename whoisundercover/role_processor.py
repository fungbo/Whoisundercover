import random

from whoisundercover.role import CIVILIAN, WHITEBOARD, UNDERCOVER
from whoisundercover.role_exception import RoleException


class RoleProcessor(object):
    INVALID_TOTAL_NUMBER = 'The number of total players can not be less than 3'
    INVALID_UNDERCOVER_NUMBER = 'The number of undercover must be less than the half of total number'

    def __init__(self, total_num, undercover_num):
        super(RoleProcessor, self).__init__()
        if total_num < 3:
            raise RoleException(msg=self.INVALID_TOTAL_NUMBER)

        if undercover_num > (total_num / 2):
            raise RoleException(msg=self.INVALID_UNDERCOVER_NUMBER)

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

        whiteboard = players.pop(random.randint(1, len(players) - 1))
        undercovers = [players.pop(random.randint(0, len(players) - 1)) for _ in range(self.undercover_num)]

        return whiteboard, undercovers


def generate_the_first_player(role_list):
    while True:
        index = random.randint(0, len(role_list) - 1)
        if role_list[index] != WHITEBOARD:
            return index
