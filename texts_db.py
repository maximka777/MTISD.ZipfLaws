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


class Text:
    def __init__(self, file_name, rubric, text, locale):
        self.rubric = rubric
        self.text = text
        self.locale = locale
        self.keywords = []
        self.file_name = file_name

    def __repr__(self):
        return 'Text{ file name: %s, rubric: %s, text: %s, locale: %s }' % (self.file_name, self.rubric,
                                                                            self.text[:20] + '...',
                                                                            self.locale)


def get_text(text):
    return text.text


def get_rubric(text):
    return text.rubric


class TextsDatabase:
    def __init__(self, texts_directory_path):
        self.texts_directory_path = texts_directory_path
        self.texts = []
        self.read_texts()

    def read_texts(self):
        current_cwd = os.getcwd()
        os.chdir(self.texts_directory_path)
        for locale in LOCALES:
            os.chdir(locale)
            rubrics = os.listdir('.')
            for rubric in rubrics:
                os.chdir(rubric)
                file_names = os.listdir('.')
                for file_name in file_names:
                    try:
                        with open(file_name, 'r', encoding='utf-8') as file:
                            self.texts.append(Text(file_name, rubric, file.read(), locale))
                    except OSError as e:
                        print('Error during reading file', file_name, e)
                os.chdir('..')
            os.chdir('..')
        os.chdir(current_cwd)

    def get_texts_by_locale(self, locale):
        return list(filter(lambda x: x.locale == locale, self.texts))
