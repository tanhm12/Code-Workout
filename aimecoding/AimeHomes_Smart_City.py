import math
import os
import random
import re
import sys


# parent = [i for i in range(n+1)]
# size = [1 for i in range(n+1)]

def find_parent(i, parent):
    if parent[i] == i:
        return i
    else:
        return find_parent(parent[i], parent)


def merge(i, j, parent, size):
    c1 =  find_parent(i, parent)
    c2 = find_parent(j, parent)
    if c1 != c2:
        if size[c1] > size[c2]:
            c1, c2 = c2, c1
        size[c2] += size[c1]
        parent[c1] = c2



def build(n, m, cost_mall, cost_road, residential_areas):
    # print(n, m, cost_mall, cost_road, residential_areas)
    if cost_mall <= cost_road:
        return cost_mall * n
    else:
        parent = [i for i in range(n+1)]
        size = [1 for i in range(n+1)]
        for u, v in residential_areas:
            merge(u, v, parent, size)
        
        group = set()
        res = 0
        for i in range(1, n+1):
            p = find_parent(i, parent)
            if p not in group:
                res += cost_road * (size[p] - 1) + cost_mall
                group.add(p)
        
        return res


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        cost_mall = int(first_multiple_input[2])

        cost_road = int(first_multiple_input[3])

        residential_areas = []

        for _ in range(m):
            residential_areas.append(list(map(int, input().rstrip().split())))
        
        print(build(n, m, cost_mall, cost_road, residential_areas))