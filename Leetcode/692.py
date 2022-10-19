from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int):
        from heapq import heapify, heappop
        from collections import Counter
        
        counter = Counter(words)
        counter = [(-counter[word], word) for word in counter]
        heapify(counter)
        
        return [heappop(counter)[1] for _ in range(k)]
        