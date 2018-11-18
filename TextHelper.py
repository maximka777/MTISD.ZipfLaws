import re

ru_filter = [
    "без", "вне", "для", "изо", "меж", "над", "обо", "ото", "под", "при", "про",  # предлоги
    "она", "оно", "они", "мой", "ваш", "наш", "его", "кто", "что", "чей", "где", "тот", "сей", "сам",  # местоимения
    "как", "так", "еще", "все", "ибо", "или", "тем", "чем", "тех"  # другие служебные слова
]

en_filter = [
    "the", "for", "and", "that", "this", "are",
    "how", "who", "where", "what", "whose",
    "some", "any", "not",
    "you", "your", "yours", "she", "her", "his"
]


def get_words(text_string):
    row_lines = text_string.splitlines()

    lines = list(filter(lambda l: len(l) > 0, row_lines))
    lines = list(map(lambda l: re.sub("[,.!?0-9:;a-zA-Z=&^%$#@*+{}()[\]]", "", l), lines))
    lines = list(map(lambda l: re.sub("^(\s+)", "", l), lines))
    lines = list(map(lambda l: re.sub("(\s+)$", "", l), lines))
    lines = list(map(lambda l: re.sub("-", " ", l), lines))
    lines = list(map(lambda l: re.sub("/", " ", l), lines))
    lines = list(map(lambda l: re.sub("\s\s+", " ", l), lines))

    prepared_string = ' '.join(lines).lower()
    words = prepared_string.split()
    return words


def filter_words(words):
    words = list(filter(lambda x: len(x) > 2, words))
    words = list(filter(lambda x: x not in ru_filter, words))
    words = list(filter(lambda x: x not in en_filter, words))
    return words

