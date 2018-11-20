from math import floor


class Sentence:
    def __init__(self, content, order_number):
        self.content = content
        self.order_number = order_number
        self.is_used = False


class TextReferee:
    def __init__(self, text, get_keywords_func, split_on_sentences_func):
        self.text = text
        self.get_keywords_func = get_keywords_func
        self.split_on_sentences_func = split_on_sentences_func

    @staticmethod
    def _normalize_compress_percentage(compress_percentage):
        if compress_percentage > 100:
            compress_percentage = 100
        elif compress_percentage < 0:
            compress_percentage = 0
        return compress_percentage

    @staticmethod
    def _find_sentences_with_keyword(sentences, keyword):
        return [sentence for sentence in sentences if not sentence.is_used and keyword in sentence.content.lower()]

    @staticmethod
    def _make_text_from_sentences(sentences, sorted=True):
        if sorted:
            sentences.sort(key=lambda s: s.order_number)
        return ' '.join(map(lambda s: s.content, sentences))

    @staticmethod
    def _get_compressed_text_length(sentences):
        return len(TextReferee._make_text_from_sentences(sentences, False))

    # NOTE: do_it because I don't know how to name this func
    def do_it(self, compress_percentage):
        full_text_volume = len(self.text)
        compress_percentage = self._normalize_compress_percentage(compress_percentage)
        needed_text_volume = floor(full_text_volume * compress_percentage / 100)
        keywords = self.get_keywords_func(self.text)
        sentences = self.split_on_sentences_func(self.text)
        sentences_for_compressed_text = []
        for keyword in keywords:
            sentences_with_keyword = self._find_sentences_with_keyword(sentences, keyword)
            for sentence in sentences_with_keyword:
                sentences_for_compressed_text.append(sentence)
                sentence.is_used = True
                if self._get_compressed_text_length(sentences_for_compressed_text) >= needed_text_volume:
                    break
        return self._make_text_from_sentences(sentences_for_compressed_text)
