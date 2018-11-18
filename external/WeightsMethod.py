from external.InverseFrequency import InverseFrequency
from external.WordFrequency import WordFrequency
from utility import get_words_from_text, filter_words


class WeightsMethod:
    def __init__(self, texts, low_weight=1):
        self.words_matrix = []
        self.words_total_matrix = []
        self.word_inverse_frequencies = []
        self.word_frequencies_matrix = []
        self.low_weight = low_weight

        for text in texts:
            text_words = filter_words(get_words_from_text(text))
            self.words_matrix.append(text_words)
            self.words_total_matrix.append(len(text_words))

        self.texts_total = len(texts)
        for x in range(self.texts_total):
            self.word_frequencies_matrix.append([])

    def get_key_words(self):
        self.calc_inverse_frequencies()
        self.calc_texts_frequencies()
        self.calc_word_weights()
        self.sort_frequencies_by_weight()

        key_words = []

        for x in range(len(self.word_frequencies_matrix)):
            print("==== Text #{} key words".format(x))
            key_words.append([])
            text_frequencies = self.word_frequencies_matrix[x]
            for freq in text_frequencies:
                if freq.weight >= self.low_weight:
                    key_words[x].append(freq.word)
                    print('[{}] k_i={}'.format(freq.word, freq.weight))

        return key_words

    def calc_inverse_frequencies(self):
        for x in range(self.texts_total):
            words = self.words_matrix[x]
            for word in words:
                inverse_frequency = self.get_inverse_frequency(word)
                if inverse_frequency is None:
                    inverse_frequency = InverseFrequency(word, x, self.texts_total)
                    self.word_inverse_frequencies.append(inverse_frequency)
                else:
                    inverse_frequency.add_text(x)

    def calc_texts_frequencies(self):
        for text_number in range(self.texts_total):
            words = self.words_matrix[text_number]
            for word in words:
                text_frequency = self.get_word_frequency(word, text_number)
                if text_frequency is None:
                    text_frequency = WordFrequency(word, len(word))
                    self.word_frequencies_matrix[text_number].append(text_frequency)
                else:
                    text_frequency.add()

    def calc_word_weights(self):
        for text_number in range(self.texts_total):
            text_frequencies = self.word_frequencies_matrix[text_number]
            for frequency in text_frequencies:
                inverse_frequency = self.get_inverse_frequency_for_word(frequency.word)
                frequency.set_inverse_frequency(inverse_frequency)
                frequency.set_weight(inverse_frequency)

    def sort_frequencies_by_weight(self):
        for freq_array in self.word_frequencies_matrix:
            freq_array.sort(key=lambda x: x.weight, reverse=True)

    def get_inverse_frequency(self, word):
        inverse_frequency = None
        for inv_freq in self.word_inverse_frequencies:
            if inv_freq.is_for_word(word):
                inverse_frequency = inv_freq
        return inverse_frequency

    def get_word_frequency(self, word, text_number):
        word_frequency = None
        for freq in self.word_frequencies_matrix[text_number]:
            if freq.is_for_word(word):
                word_frequency = freq
        return word_frequency

    def get_inverse_frequency_for_word(self, word):
        inverse_frequency = 1
        for freq in self.word_inverse_frequencies:
            if freq.is_for_word(word):
                inverse_frequency = freq.get_inverse_frequency()
        return inverse_frequency

