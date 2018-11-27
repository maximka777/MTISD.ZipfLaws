import numpy

from external.perceptron import Perceptron
from external_adapters import get_key_words_from_texts
from utility import get_texts, word_frequency, flat_nested_2


def cut_key_words(words, n=3):
    return words[:n]


class TextRubricator:
    def __init__(self, training_texts):
        self.training_texts = training_texts
        self.training_texts_attributes_vectors = []
        self.attributes = []
        self.unique_rubrics = []
        self.perceptrons = []

    def init(self):
        self._init_attributes()
        self._init_unique_rubrics()
        self._init_perceptrons()
        self._init_training_texts_attributes_vectors()

    def _init_attributes(self):
        keywords = list(map(cut_key_words, get_key_words_from_texts(get_texts(self.training_texts))))
        self.attributes = flat_nested_2(keywords)
        print('Attributes:', self.attributes)

    def _init_unique_rubrics(self):
        self.unique_rubrics = []
        for rubric in list(map(lambda t: t.rubric, self.training_texts)):
            if rubric not in self.unique_rubrics:
                self.unique_rubrics.append(rubric)
        print('Rubrics:', self.unique_rubrics)

    def _init_perceptrons(self):
        self.perceptrons = \
            [Perceptron(len(self.attributes), epochs=10000, learning_rate=0.1) for _ in range(len(self.unique_rubrics))]

    def _init_training_texts_attributes_vectors(self):
        for text in self.training_texts:
            # attributes_vector = [word_frequency(word, text.text) for word in self.attributes]
            # XXX: used 1 instead of frequency
            attributes_vector = [1 if word in text.text else 0 for word in self.attributes]
            self.training_texts_attributes_vectors.append(attributes_vector)

    def train(self):
        for rubric_idx, perceptron in enumerate(self.perceptrons):
            rubric = self.unique_rubrics[rubric_idx]
            outputs = list(map(int, [rubric == text.rubric for text in self.training_texts]))
            perceptron.train(numpy.array(self.training_texts_attributes_vectors), numpy.array(outputs))

    def rubricate(self, testing_texts):
        probabilities = []
        keywords_by_text = get_keywords(testing_texts)
        for text_id, text in enumerate(testing_texts):
            keywords = keywords_by_text[text_id]
            # XXX: used 1 instead of frequency
            # [word_frequency(word, text.text) if word in keywords else 0 for word in self.attributes]
            text_attributes_vector = \
                [1 if word in keywords else 0 for word in self.attributes]
            percetrons_outputs = [perceptron.predict(text_attributes_vector) for perceptron in self.perceptrons]
            max_perceptron_value = max(percetrons_outputs)
            max_perceptron_value_idx = percetrons_outputs.index(max_perceptron_value)
            text.rubric = self.unique_rubrics[max_perceptron_value_idx]
            probabilities.append(max_perceptron_value)
        return testing_texts, probabilities


def get_keywords(texts):
    keywords = [[None]]
    low_weight = 1
    while sum(map(lambda words: len(words), keywords)) / len(keywords) < 3 and low_weight > 0.1:
        keywords = get_key_words_from_texts(get_texts(texts))
        low_weight /= 2
    return keywords

