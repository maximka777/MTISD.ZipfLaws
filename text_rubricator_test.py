from text_rubricator import TextRubricator
from texts_db import TextsDatabase, RU


def is_not_rubricated(text):
    return text.rubric.startswith('unknown')


def is_rubricated(text):
    return not is_not_rubricated(text)


def main():
    texts_db = TextsDatabase()
    ru_texts = texts_db.get_texts_by_locale(RU)
    training_texts = list(filter(is_rubricated, ru_texts))
    testing_texts = list(filter(is_not_rubricated, ru_texts))
    text_rubricator = TextRubricator(training_texts)
    text_rubricator.init()
    text_rubricator.train()
    print(text_rubricator.rubricate(testing_texts))


if __name__ == '__main__':
    main()
