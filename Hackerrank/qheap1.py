from queue import PriorityQueue

read_int = lambda : list(map(int, input().split()))

Q = read_int()[0]
q = PriorityQueue()

res = []
deleted = set()
for i in range(Q):
    query = read_int()
    if query[0] == 1:
        q.put(query[1])
    elif query[0] == 2:
        deleted.add(query[1])
    else:
        while q.queue[0] in deleted:
            deleted.remove(q.get())
        res.append(q.queue[0])

for item in res :
    print(item)
    