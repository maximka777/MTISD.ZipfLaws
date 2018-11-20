from external.RankInfo import RankInfo
from external.WordFrequency import WordFrequency
from utility import get_words_from_text, filter_words


def get_middle_index(items_number):
    return (items_number-1)//2


class SecondLaw:
    def __init__(self, text):
        words = get_words_from_text(text)
        self.filtered_words = filter_words(words)
        self.words_total = len(self.filtered_words)
        self.low_rank = None
        self.high_rank = None
        self.sorted_counts = []
        self.sorted_frequencies = []
        self.word_frequencies = []
        self.rank_info = []
        self.key_words = []

    def calc_parameters(self):
        self.calc_frequencies()
        self.sort_frequencies()
        self.save_rank_info()

        self.define_rank_range()

        for x in range(self.low_rank, self.high_rank):
            for rank_word in self.rank_info[x].words:
                self.key_words.append(rank_word)

    def calc_frequencies(self):
        for word in self.filtered_words:
            frequency = self.get_word_frequency(word)
            if frequency is None:
                frequency = WordFrequency(word, self.words_total)
                self.word_frequencies.append(frequency)
            else:
                frequency.add()

    def get_word_frequency(self, word):
        word_frequency = None
        for freq in self.word_frequencies:
            if freq.is_for_word(word):
                word_frequency = freq
        return word_frequency

    def sort_frequencies(self):
        for freq in self.word_frequencies:
            freq_count = freq.get_count()
            if freq_count not in self.sorted_counts:
                self.sorted_counts.append(freq_count)
        self.sorted_counts.sort(reverse=True)
        self.sorted_frequencies = list(map(lambda x: x / self.words_total, self.sorted_counts))

    def save_rank_info(self):
        ranks_count = len(self.sorted_frequencies)
        for x in range(ranks_count):
            new_rank = RankInfo(self.sorted_counts[x], self.sorted_frequencies[x], x + 1)
            new_rank.set_words(self.get_words_by_frequency(new_rank.get_count()))
            self.rank_info.append(new_rank)

    def get_words_by_frequency(self, count):
        words_info = list(filter(lambda x: x.has_count(count), self.word_frequencies))
        return list(map(lambda x: x.get_word(), words_info))

    def get_graph_info(self):
        x_vector = []
        y_vector = []
        for item in self.rank_info:
            x_vector.append(item.frequency)
            y_vector.append(len(item.words))
        return [
            x_vector,
            y_vector
        ]

    def define_rank_range(self):
        ranks_number = len(self.sorted_frequencies)
        if ranks_number == 1:
            self.low_rank = 0
            self.high_rank = 1

        elif ranks_number == 2:
            self.low_rank = 0
            self.high_rank = 2

        elif ranks_number == 3:
            self.low_rank = 1
            self.high_rank = 2

        elif ranks_number == 4:
            self.low_rank = 1
            self.high_rank = 3

        else:
            self.low_rank = 2
            self.high_rank = 4

            range_a, range_b = self.get_ranks_range(ranks_number)
            self.low_rank = range_a
            if self.low_rank < 0:
                self.low_rank = 0
            self.high_rank = range_b
            if self.high_rank > ranks_number:
                self.high_rank = ranks_number

    @staticmethod
    def get_ranks_range(ranks_number):
        return int(ranks_number / 3), int(ranks_number * 2 / 3)

    def get_key_words(self):
        return self.key_words

