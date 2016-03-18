from unittest import TestCase

from mock import patch, MagicMock

from whoisundercover.data_reader import DataReader
from whoisundercover.words_selector import WordsSelector


class WordsSelectorTest(TestCase):
    @patch('random.randint')
    def test_should_get_a_pair_of_words(self, mock_randint):
        mock_randint.return_value = 0
        self.assertEqual(WordsSelector._get_a_pair_of_words_by_random(
            DataReader('./data/words.txt').get_words_list()), ['test1', 'test2'])

    @patch('random.randint', MagicMock(side_effect=[1, 0]))
    def test_should_get_undercover_and_civilian_word(self):
        self.selector = WordsSelector(DataReader('./data/words.txt').get_words_list())

        self.assertEqual(self.selector.get_undercover_word(), 'test3')
        self.assertEqual(self.selector.get_civilian_word(), 'test4')
