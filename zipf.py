from graphics_drawer import GraphicsDrawer


def zipf_constant(word_count, total_count, rank):
    return word_count * rank / total_count


def count_words_probability(counter):
    total = sum([val for val in counter.values()])
    for key in counter.keys():
        counter[key] = counter[key] / total
    return counter


def count_words(words):
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    return counter


def make_zipf_parameters_string(word_count, total_count, rank):
    return '%s = %s * %s / %s' % (zipf_constant(word_count, total_count, rank), word_count, rank, total_count)


def first_zipf_rule(words):
    counters = []
    # for words from each text
    for text_words in words:
        words_counter = count_words(text_words)
        total_words = len(text_words)

        # making array of lists with unique word counts and with one word from each rank-group
        unique_ranks_values = []
        unique_ranks_words = []
        for word, word_count in words_counter.items():
            if word_count not in unique_ranks_values:
                unique_ranks_values.append(word_count)
                unique_ranks_words.append(word)
        rank_count_pairs = list(zip(unique_ranks_words, unique_ranks_values))
        rank_count_pairs.sort(key=lambda i: -i[1])
        unique_ranks_values.sort(key=lambda a: -a)

        # printing parameters of 1st Zipf's rule
        print('-------------------------------------------------------')
        print('Words:\n', rank_count_pairs)
        for rank_number, rank_value in enumerate(unique_ranks_values):
            print(make_zipf_parameters_string(rank_value, total_words, rank_number + 1))
        print('-------------------------------------------------------')

        counters.append(count_words_probability(words_counter))
    # drawing of graphics
    for counter in counters:
        probabilities = list(counter.values())
        probabilities.sort(key=lambda a: a * -1)
        GraphicsDrawer.draw(range(len(counter)), probabilities)
    return counters


def second_zipf_rule(words):
    pass