from unittest import TestCase

from whoisundercover.role_processor import RoleProcessor
from whoisundercover.undercover_exception import UndercoverException


class RoleProcessorTest(TestCase):
    EXCEPTION_NOT_THROWN = 'exception not thrown'

    def test_should_set_total_number_of_player_and_valid_undercover_number(self):
        with self.assertRaisesRegexp(Exception, self.EXCEPTION_NOT_THROWN):
            RoleProcessor(total_num=8, undercover_num=2)
            self.fail(self.EXCEPTION_NOT_THROWN)

    def test_should_set_total_number_of_player_and_invalid_undercover_number(self):
        with self.assertRaisesRegexp(UndercoverException, RoleProcessor.INVALID_UNDERCOVER_NUMBER):
            RoleProcessor(total_num=8, undercover_num=5)
            self.fail(self.EXCEPTION_NOT_THROWN)
