def stockmax(prices):
    from heapq import heapify, heappop
    if len(prices) <= 1:
        return 0

    # pref_sum = [0]
    # for item in prices:
    #     pref_sum.append(pref_sum[-1] + item)
    
    summit = [(-prices[i], i) for i in range(len(prices))]   
    heapify(summit)
    
    total_profit = 0
    cur = 0
    while True:
        s, pos = heappop(summit)
        print(s, pos)
        if pos < cur:
            continue
        s = -s
        
        buy = 0
        for i in range(cur, pos):
            buy += prices[i]
        
        total_profit += (pos - cur) * s - buy
        
        cur = pos + 1
        if cur >= len(prices):
            break
    
    return total_profit


prices = [5,3,2]
prices = [1,2,100]

print(stockmax(prices))

    

