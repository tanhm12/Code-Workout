#!/bin/python3

import math
import os
import random
import re
import sys


def display(n):
    items = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    cur = n
    for i0 in range(2):
        cans1 = list(range(10)) if i0 != 2 else list(range(3))
        cur -= items[i0]
        for i1 in cans1:
            cur -= items[i1]
            for i2 in list(range(6)):
                cur -= items[i2]
                for i3 in list(range(10)):
                    cur -= items[i3]
                    if cur == 0:
                        print(f"{i0}{i1}:{i2}{i3}")
                        return
                    cur += items[i3]
                cur += items[i2]
            cur += items[i1]
        cur += items[i0]
    print("Impossible")


if __name__ == '__main__':
    n = int(input().strip())
    display(n)