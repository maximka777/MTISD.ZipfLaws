from external.WeightsMethod import WeightsMethod
from texts_db import *

texts_db = TextsDatabase()
weights_method = WeightsMethod(map(get_text, texts_db.get_texts_by_locale(RU)))
print('Key words', weights_method.get_key_words())
