from typing import List


def minimumLengthEncoding(words: List[str]):
    reversed_words = [item[::-1] for item in words]
    sorted_reversed_words = sorted(reversed_words) 
    
    start = 0
    
    words_in_res = [sorted_reversed_words[0]]
    for i in range(1, len(sorted_reversed_words)):
        if  sorted_reversed_words[i].startswith(words_in_res[-1]):
            words_in_res[-1] = sorted_reversed_words[i]
        else:
            words_in_res.append(sorted_reversed_words[i])
    
    # print([item[::-1] for item in words_in_res])
    return len('#'.join(words_in_res)) + 1


print(minimumLengthEncoding(["time", "me", "bell"]))

print(minimumLengthEncoding(["t"]))
    