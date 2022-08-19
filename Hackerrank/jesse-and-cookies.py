def cookies(k, A):
    from heapq import heapify, heappop, heappush
    heapify(A)
    
    if A[0] >= k:
        return 0
    
    res = 0
    
    while len(A) > 1:
        new_cookie = heappop(A) + 2 * heappop(A)
        heappush(A, new_cookie)
        res += 1
        if A[0] >= k :
            return res
    
    return -1
    