read_int = lambda : list(map(int, input().split()))

n ,q = read_int()

parent = [i for i in range(n+1)]
size = [1 for i in range(n+1)]


def find_community(i):
    if parent[i] == i:
        return i
    else:
        p = find_community(parent[i])
        parent[i] = p
        return p


def merge(i, j):
    c1 =  find_community(i)
    c2 = find_community(j)
    if c1 != c2:
        if size[c1] > size[c2]:
            c1, c2 = c2, c1
        size[c2] += size[c1]
        parent[c1] = c2
    

for i in range(q):
    inputs = input().split()
    if inputs[0] == "M":
        merge(*list(map(int, inputs[1:])))
    else:
        print(size[find_community(int(inputs[1]))])
    