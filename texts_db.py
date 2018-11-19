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


class Text:
    def __init__(self, rubric, text):
        self.rubric = rubric
        self.text = text

    def __repr__(self):
        return 'Text{ rubric: %s, text: %s }' % (self.rubric, self.text[:30] + '...')


def get_text(text):
    return text.text


class TextsDatabase:
    def __init__(self):
        self.texts = {
            RU: [],
            EN: [],
            BY: []
        }
        self.read_texts()

    @staticmethod
    def get_rubric(file_name):
        return file_name.split('_')[0]

    def read_texts(self):
        os.chdir(TEXTS_DIR)
        file_names = os.listdir('.')
        for file_name in file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    rubric = self.get_rubric(file_name)
                    self.texts[get_file_locale(file_name)].append(Text(rubric, file.read()))
            except OSError as e:
                print('Error during reading file', file_name, e)

    def get_texts_by_locale(self, locale):
        return self.texts[locale]
