import re

from external_adapters import get_key_words_from_texts
from referee.text_referee import TextReferee, Sentence
from texts_db import TextsDatabase, RU
from utility import get_texts

REGEXP_FOR_SPLITTING_ON_SENTENCES = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'


def split_on_sentences(text):
    return [Sentence(sentence.strip(), idx)
            for idx, sentence in enumerate(re.split(REGEXP_FOR_SPLITTING_ON_SENTENCES, text))]


def save_text_to_file(text):
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    texts_db = TextsDatabase('../TextsForTesting/RubricatorTexts')

    ru_texts = texts_db.get_texts_by_locale(RU)

    text_number = 0

    percent = int(input('Percentage: '))

    def get_key_words_from_text(text):
        return get_key_words_from_texts(get_texts(ru_texts), 100)[text_number]

    referee = TextReferee(ru_texts[text_number].text, get_key_words_from_text, split_on_sentences)
    save_text_to_file(referee.do_it(percent))


if __name__ == '__main__':
    main()
