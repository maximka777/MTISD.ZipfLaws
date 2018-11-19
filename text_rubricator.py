import numpy

from external.WeightsMethod import WeightsMethod
from external.perceptron import Perceptron
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
        keywords = list(map(cut_key_words, WeightsMethod(get_texts(self.training_texts)).get_key_words()))
        self.attributes = flat_nested_2(keywords)

    def _init_unique_rubrics(self):
        self.unique_rubrics = []
        for rubric in list(map(lambda t: t.rubric, self.training_texts)):
            if rubric not in self.unique_rubrics:
                self.unique_rubrics.append(rubric)

    def _init_perceptrons(self):
        self.perceptrons = [Perceptron(len(self.attributes)) for _ in range(len(self.unique_rubrics))]

    def _init_training_texts_attributes_vectors(self):
        for text in self.training_texts:
            attributes_vector = [word_frequency(word, text.text) for word in self.attributes]
            self.training_texts_attributes_vectors.append(attributes_vector)

    def train(self):
        for rubric_idx, perceptron in enumerate(self.perceptrons):
            rubric = self.unique_rubrics[rubric_idx]
            outputs = list(map(int, [rubric == text.rubric for text in self.training_texts]))
            perceptron.train(numpy.array(self.training_texts_attributes_vectors), numpy.array(outputs))

    def rubricate(self, testing_texts):
        probabilities = []
        for text in testing_texts:
            text_attributes_vector = [word_frequency(word, text.text) for word in self.attributes]
            percetrons_outputs = [perceptron.predict(text_attributes_vector) for perceptron in self.perceptrons]
            max_perceptron_value = max(percetrons_outputs)
            max_perceptron_value_idx = percetrons_outputs.index(max_perceptron_value)
            text.rubric = self.unique_rubrics[max_perceptron_value_idx]
            probabilities.append(max_perceptron_value)
        return testing_texts, probabilities
