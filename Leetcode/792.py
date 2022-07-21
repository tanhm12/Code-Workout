from typing import List

def numMatchingSubseq(s: str, words: List[str]):
    from collections import defaultdict
    all_pos = defaultdict(list)
    
    for i, c in enumerate(s):
        all_pos[c].append(i)
        
    all_pos = dict(all_pos)
    
    import bisect
    
    res = 0
    
    for word in words:
        if word[0] not in all_pos:
            continue
        prev_id = all_pos[word[0]][0]
        is_valid = True
        for i in range(1, len(word)):
            if word[i] not in all_pos:
                is_valid = False
                break
            current_all_pos = all_pos[word[i]]
            # print(current_all_pos)
            pos = bisect.bisect(current_all_pos, prev_id)
            # print(pos, prev_id, current_all_pos)
            if pos >= len(current_all_pos):
                is_valid = False
                break
            prev_id = current_all_pos[pos]
        if is_valid:
            res += 1
    
    return res
    
# print(numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
print(numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
