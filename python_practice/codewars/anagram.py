def anagrams(word, words):
    word_list = list(word)
    new_list = []
    for w in range(len(words)):
        k = sorted(list(words[w]))
        if k == sorted(word_list):
            new_list.append(words[w])

    return new_list
