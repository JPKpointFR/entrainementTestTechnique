# trouver le mot le plus court et le plus long

# ordre dans la phrase en premier
def get_min_max_words(sentense):
    words = sentense.split()
    # print(words)
    min_word = min(words, key=len)
    max_word = max(words, key=len)

    return min_word, max_word

# ordre alphabétique en premier


def get_min_max_words_sorted(sentense):
    words = sentense.split(" ")
    min_word, max_word = get_min_max_words(sentense)

    all_min_words = [w for w in words if len(w) == len(min_word)]
    all_max_words = [w for w in words if len(w) == len(max_word)]

    all_min_words.sort()
    all_max_words.sort()

    return all_min_words[0], all_max_words[0]


def get_min_max_words_sorted2(sentense):
    words = sentense.split(" ")
    words.sort()
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    return min_word, max_word


s = "Un chasseur sachant chasser sait chasser sans son chien"

min_word, max_word = get_min_max_words_sorted2(s)

print(f"Mots le plus petit: {min_word}")
print(f"Mots le plus grand: {max_word}")
