def isHappy(n: int):
    if n == 1:
        return True
    digit_square = {str(i): i**2 for i in range(10)}
    
    res_set = set([n])
    while True:
        cur = sum([digit_square[i] for i in str(n)])
        if cur == 1:
            return True
        
        if cur in res_set:
            return False
        else:
            res_set.add(cur)
            n = cur

print(isHappy(19))
    
    