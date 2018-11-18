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

    def set_weight(self, inverse_frequency):
        self.weight = self.get_frequency() * inverse_frequency

    def set_inverse_frequency(self, inverse_frequency):
        self.inverse_frequency = inverse_frequency

    def get_frequency(self):
        return self.count / self.total

    def get_count(self):
        return self.count

    def get_word(self):
        return self.word
