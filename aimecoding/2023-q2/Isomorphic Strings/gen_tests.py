from .solution import Solution
    
tests = [
    ["aaabbbab", "bbbaaaab", False],
    ["aaabbbabba", "bbbaaaabab", False],
]

import random
rd = random.Random(122)
characters = [chr(i + 97) for i in range(26)]

def gen_tests_true(length):
    sequences = []
    cur_sum = 0
    
    for c in characters:
        num = rd.randint(0, length//2)
        if num + cur_sum > length:
            break
        cur_sum += num
        sequences.append(num)
    seed = rd.randint(0, 100)
    def  make_string():
        res = []
        chars = rd.sample(characters, k=len(characters))
        for i in range(len(sequences)):
            res.append(chars[i] * sequences[i])
        random.seed(seed)
        res = list("".join(res))
        random.shuffle(res)
        return "".join(res)
    
    return [make_string(), make_string(), True]

for i in range(10):
    tests.append(gen_tests_true(rd.randint(5, 50000)))
    x, y, res = tests[-1]
    assert Solution().isIsomorphic(x, y) == res


for i in range(10):
    seq1 = ["".join(rd.sample(characters, 10)) for _ in range(rd.randint(5, 50000))]
    x, y = "".join(seq1), "".join(rd.sample(seq1, len(seq1)))
    tests.append([x, y,  Solution().isIsomorphic(x, y)])


import os 
def dump_inp(test, i,  folder="test_cases/input"):
    with open(os.path.join(folder, f"input{str(i).zfill(2)}.txt"), "w") as f:
        f.write(f'{test[0]}\n{test[1]}')

def dump_out(test, i,  folder="test_cases/output"):
    with open(os.path.join(folder, f"output{str(i).zfill(2)}.txt"), "w") as f:
        f.write(f'{test[2]}')
        
    
for i in range(len(tests)):
    dump_inp(tests[i], i)
    dump_out(tests[i], i)
