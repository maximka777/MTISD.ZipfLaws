import re

from external_adapters import get_key_words_from_text
from referee.text_referee import TextReferee, Sentence
from texts_db import TextsDatabase, RU

REGEXP_FOR_SPLITTING_ON_SENTENCES = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'


def split_on_sentences(text):
    return [Sentence(sentence.strip(), idx)
            for idx, sentence in enumerate(re.split(REGEXP_FOR_SPLITTING_ON_SENTENCES, text))]


def save_text_to_file(text):
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    texts_db = TextsDatabase('../texts')
    referee = TextReferee(texts_db.get_texts_by_locale(RU)[0].text, get_key_words_from_text, split_on_sentences)
    save_text_to_file(referee.do_it(50))


if __name__ == '__main__':
    main()
