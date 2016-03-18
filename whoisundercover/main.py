import random

from whoisundercover.data_reader import DataReader
from whoisundercover.role_processor import RoleProcessor
from whoisundercover.words_selector import WordsSelector

INVALID_NUMBER = 'The number must be digit'


def play():
    total_num = raw_input('Input the number of total players:')
    if not total_num.isdigit():
        print INVALID_NUMBER

    undercover_num = raw_input('Input the number of undercovers:')
    if not undercover_num.isdigit():
        print INVALID_NUMBER

    role_processor = RoleProcessor(int(total_num), int(undercover_num))
    role_list = role_processor.assign_role_to_player()

    words_selector = WordsSelector(DataReader('./data/words.txt').get_words_list())
    words = words_selector.get_a_pair_of_words_by_random()
    undercover_word_index = random.randint(0, len(words) - 1)

    print role_list, words, undercover_word_index

if __name__ == '__main__':
    play()
