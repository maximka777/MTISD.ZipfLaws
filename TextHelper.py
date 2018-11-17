import re


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
    print("Words:")
    print(words)
    return words

