t = int(input())
 
def solve():
    n = int(input())
    current_sol = set()
    
    def get(i, current_sum):
        if current_sum == 0:
            return True
        for i in range(9, 0, -1):
            if i not in current_sol and i <= current_sum:
                current_sol.add(i)
                found = get(i + 1, current_sum=current_sum-i)
                if found:
                    return True
                current_sol.remove(i)
    get(0, n)
    return ''.join(list(map(str, sorted(current_sol))))
 
res = []
for i in range(t):
    res.append(solve())
 
for i in res:
    print(i)