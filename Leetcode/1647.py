def minDeletions(s: str):
    from collections import defaultdict
    
    freq = defaultdict(int)
    for i in s:
        freq[i] += 1
    
    inverse_freq = defaultdict(int)
    for k in freq:
        inverse_freq[k] += 1
    