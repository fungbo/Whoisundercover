

class DataReader(object):
    def __init__(self, path):
        super(DataReader, self).__init__()
        self.path = path

    def read(self):
        with open(self.path) as data:
            return data.read().rstrip('\n')

    def get_all_words(self):
        words_str = self.read()
        words_list = [row.split(',') for row in words_str.split('\n')]

        res = []
        for words in words_list:
            res.append(map(lambda word: word.strip(), words))
        return res
