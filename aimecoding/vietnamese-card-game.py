#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def check(cards):
    all_cards = list(map(str, range(3,10))) + ["T", "J", "Q", "K", "A", "2"]
    all_cards = {all_cards[i]: i for i in range(len(all_cards))}
    
    counter = defaultdict(int)
    # print(cards)
    for c in cards:
        counter[all_cards[c[0]]] += 1
    
    if counter[all_cards["2"]] == 4:
        return True
    
    # print(counter)
    if len(counter) == 13:
        return True
    
    items = sorted(list(counter.items()))
    count = 0
    for c, num in items:
        if num >= 2:
            count += 1
            if count == 5:
                return True
        else:
            count = 0
    
    count = 0
    for c, num in items:
        if num >= 2:
            count += 1
            if count == 6:
                return True
    
    return False


if __name__ == '__main__':

    cards = []
    for i in range(13):
        cards.append(input().rstrip())
    
    if check(cards):
        print("YES")
    else:
        print("NO")
    
    