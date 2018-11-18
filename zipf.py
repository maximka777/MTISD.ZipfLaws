from graphics_drawer import GraphicsDrawer
from utility import count_words_probability


def first_zipf_rule(words):
    counters = []
    for text_words in words:
        counters.append(count_words_probability(text_words))
    for counter in counters:
        probabilities = list(counter.values())
        probabilities.sort(key=lambda a: a * -1)
        GraphicsDrawer.draw(range(len(counter)), probabilities)
    return counters


def second_zipf_rule(words):
    return words