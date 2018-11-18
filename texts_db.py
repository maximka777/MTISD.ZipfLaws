import os

FILE_EXTENSION = '.txt'

RU = 'ru'
EN = 'en'
BY = 'by'

LOCALES = [
    RU,
    EN,
    BY
]

TEXTS_DIR = './texts'


def get_file_locale(file_name):
    for locale in LOCALES:
        if file_name.endswith('_' + locale + FILE_EXTENSION):
            return locale


class TextsDatabase:
    def __init__(self):
        self.texts = {
            RU: [],
            EN: [],
            BY: []
        }
        self.read_texts()

    def read_texts(self):
        os.chdir(TEXTS_DIR)
        file_names = os.listdir('.')
        for file_name in file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    self.texts[get_file_locale(file_name)].append(file.read())
            except OSError as e:
                print('Error during reading file', file_name, e)

    def get_texts_by_locale(self, locale):
        return self.texts[locale]
