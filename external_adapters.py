from external.SecondLaw import SecondLaw
from external.WeightsMethod import WeightsMethod


def get_key_words_from_texts(texts, number):
    weights_method = WeightsMethod(texts, 0.001, number)
    return weights_method.get_keywords(True)


def get_key_words_from_text(text):
    second_law = SecondLaw(text)
    second_law.calc_parameters()
    return second_law.get_key_words()

