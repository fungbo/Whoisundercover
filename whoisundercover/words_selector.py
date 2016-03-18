import random


class WordsSelector(object):
    def __init__(self, words_list=None):
        super(WordsSelector, self).__init__()
        self.words_list = words_list

    def get_a_pair_of_words_by_random(self):
        return self.words_list[random.randint(0, len(self.words_list) - 1)]

    @staticmethod
    def get_a_word_by_random(words):
        return words[random.randint(0, len(words) - 1)]
