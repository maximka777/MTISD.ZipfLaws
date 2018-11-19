from texts_db import *
from utility import get_words_from_text
from zipf import first_zipf_rule


class ZipfMediator:
    def __init__(self):
        self.texts_db = TextsDatabase()

    def check_first_rule(self):
        ru_texts = map(get_text, self.texts_db.get_texts_by_locale(RU))
        words = [get_words_from_text(text) for text in ru_texts]
        first_zipf_rule(words)
        en_texts = map(get_text, self.texts_db.get_texts_by_locale(EN))
        words = [get_words_from_text(text) for text in en_texts]
        first_zipf_rule(words)

    def check_second_rule(self):
        pass


def get_user_option():
    print('''
1 - Zipf's 1st rule
2 - Zipf's 2st rule
0 - Quit
    ''')
    return input('Select option: ')


def main():
    zipf_mediator = ZipfMediator()
    choice = None
    while choice != '0':
        choice = get_user_option()
        if choice == '1':
            zipf_mediator.check_first_rule()
        elif choice == '2':
            zipf_mediator.check_second_rule()
        elif choice == '0':
            quit(0)


if __name__ == '__main__':
    main()
