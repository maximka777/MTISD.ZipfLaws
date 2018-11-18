import math


class InverseFrequency:
    def __init__(self, word, text_number, texts_total):
        self.word = word
        self.texts_total = texts_total
        self.texts = [text_number]

    def is_for_word(self, word):
        return self.word == word

    def add_text(self, text_number):
        if text_number not in self.texts:
            self.texts.append(text_number)

    def get_inverse_frequency(self):
        return math.log(self.texts_total / len(self.texts))

    def get_word(self):
        return self.word