
"""Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'."""

def countVowelPermutation(n: int):
    mod = int(1e9) +  7
    res = [[0 for _  in range(5)] for i in range(20007)]
    # res[0] =  [1 for i in range(5)]
    res[1] = [1 for i in range(5)]
    
    for i in range(2, n + 1):
        res[i][0] = res[i-1][1]
        res[i][1] = res[i-1][0] + res[i-1][2]
        res[i][2] = res[i-1][0] + res[i-1][1] +  res[i-1][3] + res[i-1][4]
        res[i][3] = res[i-1][2] + res[i-1][4]
        res[i][4] = res[i-1][0]
        
        for j in range(5):
            res[i][j] %= mod
    
    return sum(res[n]) % mod

print(countVowelPermutation(10000))
    