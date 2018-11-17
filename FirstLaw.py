import TextHelper
from WordFrequency import WordFrequency
from RankInfo import RankInfo


class FirstLaw:
    text_words = []
    filtered_words = []
    words_total = 0
    sorted_counts = []
    sorted_frequencies = []
    word_frequencies = []
    rank_info = []

    def __init__(self, text, low_rank, high_rank):
        self.text_words = TextHelper.get_words(text)
        self.low_rank = low_rank
        self.high_rank = high_rank
        self.filtered_words = list(filter(lambda x: len(x) > 1, self.text_words))
        self.words_total = len(self.filtered_words)

    def get_key_words(self):
        self.calc_frequencies()
        self.sort_frequencies()
        self.save_rank_info()

        return self.filtered_words

    def calc_frequencies(self):
        for word in self.filtered_words:
            frequency = self.get_word_frequency(word)
            if frequency is None:
                frequency = WordFrequency(word, self.words_total)
                self.word_frequencies.append(frequency)
            else:
                frequency.add()

    def sort_frequencies(self):
        for freq in self.word_frequencies:
            freq_count = freq.get_count()
            if freq_count not in self.sorted_counts:
                self.sorted_counts.append(freq_count)

        self.sorted_counts.sort(reverse=True)
        self.sorted_frequencies = list(map(lambda x: x / self.words_total, self.sorted_counts))

        print("Sorted frequencies:")
        print(self.sorted_frequencies)

    def save_rank_info(self):
        ranks_count = len(self.sorted_frequencies)
        for x in range(ranks_count):
            new_rank = RankInfo(self.sorted_counts[x], self.sorted_frequencies[x], x + 1)
            new_rank.set_words(self.get_words_by_frequency(new_rank.get_count()))
            self.rank_info.append(new_rank)

    def get_word_frequency(self, word):
        word_frequency = None
        for freq in self.word_frequencies:
            if freq.is_for_word(word):
                word_frequency = freq
        return word_frequency

    def get_words_by_frequency(self, count):
        words_info = list(filter(lambda x: x.has_count(count), self.word_frequencies))
        return list(map(lambda x: x.get_word(), words_info))
