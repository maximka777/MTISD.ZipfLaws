from prettytable import PrettyTable

from external.InverseFrequency import InverseFrequency
from external.WordFrequency import WordFrequency
from utility import filter_words, get_words_from_text


class WeightsMethod:
    def __init__(self, texts, lowest_weight):
        self.list_of_words_lists = []  # [[word, ...]]
        self.words_inverse_frequencies = []  # inverse frequencies of all words [inverse_frequency, ...]
        self.list_of_words_frequencies_lists = []  # [[frequency, ...]]
        self.lowest_weight = lowest_weight  # lowest weight
        self.texts_total_count = len(texts)

        self.inverse_frequencies = {}
        self.frequencies = {}

        # detecting of words in each text
        self.list_of_words_lists = list([filter_words(get_words_from_text(text)) for text in texts])

        self.list_of_words_frequencies_lists = [[] for _ in range(len(texts))]

    def get_keywords(self, log=False):
        self.calc_inverse_frequencies()
        self.calc_texts_frequencies()  # calculate frequencies for each word in each text
        self.calc_word_weights()  # calculate weights of each word in each text
        self.sort_frequencies_by_weight()

        keywords = []

        for text_idx in range(self.texts_total_count):
            if log:
                print("Keywords for %sth text:" % text_idx)
            keywords.append([])
            text_frequencies = self.frequencies[text_idx]
            items = list(text_frequencies.values())
            items.sort(key=lambda x: -x.weight)
            items = items[:20]
            table = PrettyTable()

            table.field_names = ['Word', 'Weight']

            for item in items:
                if item.weight >= self.lowest_weight:
                    keywords[text_idx].append(item.word)
                    table.add_row([item.word, item.weight])

            if log:
                print(table)

        return keywords

    def calc_inverse_frequencies(self):
        inverse_frequencies = {}
        for i in range(self.texts_total_count):
            words = self.list_of_words_lists[i]
            for word in words:
                if word not in inverse_frequencies:
                    inverse_frequencies[word] = InverseFrequency(word, i, self.texts_total_count)
                else:
                    inverse_frequencies[word].add_text(i)
        self.words_inverse_frequencies = list(inverse_frequencies.values())
        self.inverse_frequencies = inverse_frequencies

    def calc_texts_frequencies(self):
        frequencies = {}
        for text_idx in range(self.texts_total_count):
            text_frequencies = {}
            text_words = self.list_of_words_lists[text_idx]
            for word in text_words:
                if word not in text_frequencies:
                    text_frequencies[word] = WordFrequency(word, len(text_words))
                else:
                    text_frequencies[word].add()
            frequencies[text_idx] = text_frequencies
        items = list(frequencies.items())
        items.sort(key=lambda x: x[0])  # sorting by text number
        self.list_of_words_frequencies_lists = [list(val.values()) for _, val in items]
        self.frequencies = frequencies

    def calc_word_weights(self):
        for text_number in range(self.texts_total_count):
            text_frequencies = self.frequencies[text_number]
            for frequency in text_frequencies.values():
                inverse_frequency = self.get_inverse_frequency_for_word(frequency.word)
                frequency.set_inverse_frequency(inverse_frequency)  # weight calculating is inside

    def sort_frequencies_by_weight(self):
        for freq_array in self.list_of_words_frequencies_lists:
            freq_array.sort(key=lambda x: x.weight, reverse=True)

    def get_inverse_frequency(self, word):
        inverse_frequency = None
        for inv_freq in self.words_inverse_frequencies:
            if inv_freq.is_for_word(word):
                inverse_frequency = inv_freq
        return inverse_frequency

    def get_inverse_frequency_for_word(self, word):
        if word not in self.inverse_frequencies:
            return 1
        return self.inverse_frequencies[word].get_inverse_frequency()

