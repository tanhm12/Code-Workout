from solution import Solution
    
inp = [1,2,5,10] + list(range(950, 1000))
tests = []

for i in inp:
    tests.append([i,  Solution().divisorGame(i)])


import os 
os.makedirs("test_cases/input", exist_ok=True)
os.makedirs("test_cases/output", exist_ok=True)


def dump_inp(test, i,  folder="test_cases/input"):
    with open(os.path.join(folder, f"input{str(i).zfill(2)}.txt"), "w") as f:
        f.write(f'{test[0]}')

def dump_out(test, i,  folder="test_cases/output"):
    with open(os.path.join(folder, f"output{str(i).zfill(2)}.txt"), "w") as f:
        f.write(f'{test[1]}')
        
    
for i in range(len(tests)):
    dump_inp(tests[i], i)
    dump_out(tests[i], i)
