m,n,t = list(map(int, input().split()))

def is_possible(x):
    return x + x//m >= n

def find():
    x = int(n/ ( 1 + 1 /  m))
    
    if is_possible(x):
        return x
    return int((n+1) / ( 1 + 1 /  m))

print(find() * t)
            
