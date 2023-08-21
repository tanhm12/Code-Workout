def  getAnagramPeriod(input_str):
    n = len(input_str)
    from collections import Counter
    def is_possible(val):
        counter = Counter(input_str[:val])
        for i in range(val, n, val):
            if Counter(input_str[i: i+val]) != counter:
                return False
        return True
    
    for i in range(1, n):
        if n % i == 0:
            if is_possible(i):
                return i
    
    return n
    
input_str = "ababbaab"
input_str = "abcbcacba"
print(getAnagramPeriod(input_str))            