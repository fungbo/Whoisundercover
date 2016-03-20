import os
from time import sleep

from whoisundercover.data_reader import DataReader
from whoisundercover.role import ROLES, CIVILIAN, UNDERCOVER, WHITEBOARD
from whoisundercover.role_exception import RoleException
from whoisundercover.role_processor import RoleProcessor, generate_the_first_player
from whoisundercover.title import TITLE
from whoisundercover.words_selector import WordsSelector


def play():
    __show_title()

    total_num = __player_input('Input the number of total players: ')
    undercover_num = __player_input('Input the number of undercovers: ')

    try:
        role_processor = RoleProcessor(int(total_num), int(undercover_num))
        role_list = role_processor.assign_role_to_player()

        words_selector = WordsSelector(DataReader('./data/words.txt').get_words_list())
        civilian_word = words_selector.get_civilian_word()
        undercover_word = words_selector.get_undercover_word()

        __show_game_start_message()
        __show_words_to_every_player(role_list, civilian_word, undercover_word)
        __loop(role_list, generate_the_first_player(role_list))

    except RoleException, e:
        print e.msg


def __show_words_to_every_player(role_list, civilian_word, undercover_word):
    role_word = {CIVILIAN: civilian_word, UNDERCOVER: undercover_word, WHITEBOARD: '_'}

    for index, role in enumerate(role_list):
        __player_confirm('Player %s, type Y/y to see your word: ' % (index + 1))
        print 'Your word is: %s' % role_word[role]
        __player_confirm('Remember your word, then type Y/y to continue: ')


def __loop(role_list, the_first_player):
    game_round = 1
    out_players = []
    while True:
        __show_blank_line()
        print '[Round %s]' % game_round
        __show_blank_line()
        print 'Player %s, please speak.' % (the_first_player + 1)
        __show_blank_line()

        out_players = __out_player(out_players, role_list)
        if __check_if_game_over(out_players, role_list):
            __show_blank_line()
            print 'Game Over. Bye.'
            break
        game_round += 1


def __out_player(out_players, role_list):
    while True:
        __show_blank_line()
        number = __player_input('Input the number to see the role of the player:')
        if number not in out_players:
            out_players.append(number)
            print "Player %s is out and its role is '%s'" % (number, ROLES[role_list[int(number) - 1]])
            return out_players
        else:
            print 'Player %s is already out.' % number
            __show_blank_line()


def __check_if_game_over(out_players, role_list):
    out_players_roles = [role_list[int(player) - 1] for player in out_players]
    if out_players_roles.count(UNDERCOVER) == role_list.count(UNDERCOVER)\
            or out_players_roles.count(CIVILIAN) == role_list.count(CIVILIAN):
        return True

    return False


def __player_input(msg):
    while True:
        number = raw_input(msg)
        __show_blank_line()
        if number.isdigit():
            return number
        else:
            print 'The number must be digit.'


def __player_confirm(msg):
    while True:
        __show_blank_line()
        answer = raw_input(msg)
        __show_blank_line()
        if answer == 'Y' or answer == 'y':
            break
        else:
            print 'Type Y/y to continue.'


def __show_title():
    print TITLE


def __show_game_start_message():
    print 'Game start, Enjoy.'

    wait_unit_list = range(1, 4)
    wait_unit_list.reverse()
    for i in wait_unit_list:
        print '.' * i
        sleep(0.5)

    __show_blank_line()


def __show_blank_line():
    print ''


if __name__ == '__main__':
    play()
