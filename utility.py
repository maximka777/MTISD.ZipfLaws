import re

from noise_words import RU_NOISE_WORDS, EN_NOISE_WORDS, NOTICED_NOISE_WORDS
from texts_db import get_text


def make_good_word(word):
    return re.sub(r'[^A-Za-zА-Яа-я]+$', '', re.sub(r'^[^A-Za-zА-Яа-я]+', '', word)).lower()


def get_texts(texts):
    return list(map(get_text, texts))


def get_words_from_text(text):
    words = re.split('\s', text)
    return list(filter(lambda w: len(w) > 0, map(make_good_word, words)))


def is_good_word(word):
    return word not in RU_NOISE_WORDS and \
           word not in EN_NOISE_WORDS and \
           word not in NOTICED_NOISE_WORDS \
           and len(word) > 2


def filter_words(words):
    return list(filter(is_good_word, words))


def count_words_probability(words):
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    for key in counter.keys():
        counter[key] = counter[key] / len(words)
    return counter


def word_frequency(word, text):
    counter = 0
    words = get_words_from_text(text)
    for w in words:
        if w == word:
            counter += 1
    return counter / len(words)


def flat_nested_2(lists):
    return [item for lisd in lists for item in lisd]  # lisd = list
