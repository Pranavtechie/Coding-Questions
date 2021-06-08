def return_distance(list, word1, word2):
    word1_count = list.count(word1)
    word2_count = list.count(word2)
    index_word1lis = []
    index_word2lis = []
    if word1_count > 1:
        for i in range(word1_count): 
            ind = list.index(word1)
            index_word1lis.append(ind+(len(index_word1lis)))
            del list[ind]
    else:
        index_word1lis.append(list.index(word1))
    if word2_count > 1:
        for i in range(word2_count):
            ind = list.index(word2)
            index_word2lis.append(ind+(len(index_word2lis)))
            del list[ind]
    else:
        index_word2lis.append(list.index(word2))

    # index_word1 = list.index(word1)
    # index_word2 = list.index(word2)
    got_val = index_word1 - index_word2
    if got_val < 1:
        return index.word2 - index_word1


print(return_distance(["practice", "makes", "perfect",
                       "coding", "makes"], "makes", "coding"))
