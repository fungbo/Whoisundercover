from unittest import TestCase

from whoisundercover.data_reader import DataReader


class DataReaderTest(TestCase):
    def setUp(self):
        self.reader = DataReader('./data/words.txt')

    def test_should_read_data_from_file(self):
        words_str = self.reader.read()

        self.assertEqual(words_str, ' test1,test2\ntest3 , test4')

    def test_should_get_all_words(self):
        words = self.reader.get_words_list()

        self.assertEqual(words, [['test1', 'test2'], ['test3', 'test4']])
