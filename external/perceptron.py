import numpy as np


class Perceptron(object):
    def __init__(self, number_of_inputs, epochs=100, learning_rate=0.01):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.weights = np.zeros(number_of_inputs + 1)

    def predict(self, inputs):
        return np.dot(inputs, self.weights[1:]) + self.weights[0]

    def train(self, training_inputs, outputs):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, outputs):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
