from external.SecondLaw import SecondLaw


def get_key_words_from_texts(texts):
    return [get_key_words_from_text(text) for text in texts]


def get_key_words_from_text(text):
    second_law = SecondLaw(text)
    second_law.calc_parameters()
    return second_law.get_key_words()
