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
    civilian_word = words_selector.get_civilian_word()
    undercover_word = words_selector.get_undercover_word()

    print role_list, civilian_word, undercover_word


if __name__ == '__main__':
    play()
