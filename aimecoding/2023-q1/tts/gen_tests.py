class Solution:
    def isInterleave(self, a1: str, a2: str, s: str, **kwargs) -> bool:
        
        if len(s) != len(a1) + len(a2):
            return False

        dp = [[False] * (len(a2) + 1) for _ in range(len(a1) + 1)]

        for i in range(len(a1) + 1):
            for j in range(len(a2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and a2[j - 1] == s[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and a1[i - 1] == s[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and a1[i - 1] == s[i + j - 1]) or (dp[i][j - 1] and a2[j - 1] == s[i + j - 1])

        return dp[len(a1)][len(a2)]
    
    
import re

def parse():
    with open("data.txt") as f:
        data = f.read().split("\n\n")
    
    tests = []
    get_text_ptn = re.compile('"(.*)+"')
    get_text = lambda x: get_text_ptn.search(x).group()[1:-1]
    for test in data:
        test = test.split("\n")
        tests.append({
            "a1": get_text(test[1]),
            "a2": get_text(test[2]),
            "s": get_text(test[3]),
            "res": bool(test[4].split()[-1])
        })
    
    return tests


tests = parse()
    
    
import random
rd = random.Random(2)

def merge_strs(a1, a2, res=True, **kwargs):
    i1 = 0
    i2 = 0
    m = ""
    prev = 2
    while i1 < len(a1) and i2 < len(a2):
        if prev == 1:
            ni2 = rd.randint(i2+1, len(a2))
            m += a2[i2:ni2]
            i2 = ni2
            prev=2
        else:
            ni1 = rd.randint(i1+1, len(a1))
            m += a1[i1:ni1]
            i1 = ni1
            prev=1
    
    if i1 >= len(a1):
        m += a2[i2:]
    else:
        m += a1[i1:]
    
    if not res :
        if len(m) > 5:
            i = rd.randint(len(m) // 2, len(m)-1)
        else:
            i=0
        j = i+5
        shuffle = list(m[i:j])
        flag = False
        for _ in range(10):
            if "".join(shuffle) == m[i:j]:
                rd.shuffle(shuffle)
            else:
                flag = True
                break
        if not flag:
            raise ValueError()
            
        m = m[:i] + "".join(shuffle) + m[j:]
    
    assert len(m) == len(a1) + len(a2)
    assert Solution().isInterleave(a1, a2, m) == res
    return m

from tqdm import tqdm 

new_tests = [
    {"a1": "acb", "a2": "cbc", "s": "acbccb", "res": True},
    {"a1": "acb", "a2": "cbc", "s": "acbbcc", "res": False},
    {"a1": "aabcc", "a2": "dbbca", "s": "aadbbcbcac", "res": True}
]
for t in tqdm(tests):
    if len(t['a1']) + len(t['a2']) < 1:
        continue
    try:
        s = merge_strs(**t)
        t['s'] = s
        new_tests.append(t)
    except:
        pass
    
    try:
        t = dict(t.items())
        t["res"] = not t["res"]
        s = merge_strs(**t)
        t['s'] = s
        new_tests.append(t)
    except:
        pass
    
for t in new_tests:
    if Solution().isInterleave(**t) != t['res']:
        print(t)
        

import os 
def dump_inp(test, i,  folder="test_cases/input"):
    with open(os.path.join(folder, f"input{str(i).zfill(2)}.txt"), "w") as f:
        f.write(f'{test["a1"]}\n{test["a2"]}\n{test["s"]}')

def dump_out(test, i,  folder="test_cases/output"):
    with open(os.path.join(folder, f"output{str(i).zfill(2)}.txt"), "w") as f:
        f.write(f'{test["res"]}')
        
    
for i in range(len(new_tests)):
    dump_inp(new_tests[i], i)
    dump_out(new_tests[i], i)
    