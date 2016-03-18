import random


class WordsSelector(object):
    def __init__(self, words_list=None):
        super(WordsSelector, self).__init__()
        self.words = self._get_a_pair_of_words_by_random(words_list)
        self.undercover_word_index = random.randint(0, len(self.words) - 1)

    @staticmethod
    def _get_a_pair_of_words_by_random(words_list):
        return words_list[random.randint(0, len(words_list) - 1)]

    def get_undercover_word(self):
        return self.words[self.undercover_word_index]

    def get_civilian_word(self):
        return self.words[1 - self.undercover_word_index]
