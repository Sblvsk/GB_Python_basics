from random import choice, randrange

def get_jokes(n, repeat=True):

    """ Random jokes function """

    my_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if repeat:
        for i in range(n):
            my_list.append(" ".join([choice(nouns), choice(adverbs), choice(adjectives)]))
    else:
        while len(nouns):
            word_nouns = nouns.pop(randrange(len(nouns)))
            word_adverbs = adverbs.pop(randrange(len(adverbs)))
            word_adjectives = adjectives.pop(randrange(len(adjectives)))
            my_list.append(" ".join([word_nouns, word_adverbs, word_adjectives]))

    return print(my_list)

get_jokes(6, repeat=False)