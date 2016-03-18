from unittest import TestCase

from mock import patch

from whoisundercover.data_reader import DataReader
from whoisundercover.words_selector import WordsSelector


class WordsSelectorTest(TestCase):
    def setUp(self):
        self.selector = WordsSelector(DataReader('./data/words.txt').get_words_list())

    @patch('random.randint')
    def test_should_get_anyone_words(self, mock_randint):
        mock_randint.return_value = 1

        self.assertEqual(self.selector.get_a_pair_of_words_by_random(), ['test3', 'test4'])
