class WordFrequency:
    def __init__(self, word, total):
        self.word = word
        self.total = total
        self.count = 1
        self.weight = None
        self.inverse_frequency = None

    def is_for_word(self, word):
        return self.word == word

    def has_count(self, count):
        return self.count == count

    def add(self):
        self.count = self.count + 1

    def calc_weight(self):
        self.weight = self.get_frequency() * self.inverse_frequency

    def set_inverse_frequency(self, inverse_frequency):
        self.inverse_frequency = inverse_frequency
        self.calc_weight()

    def get_frequency(self):
        return self.count / self.total

    def get_count(self):
        return self.count

    def get_word(self):
        return self.word
