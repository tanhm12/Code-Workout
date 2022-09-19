from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]):
        all_dirs = []
        res = defaultdict(list)
        for path in paths:
            cur =  path.split()
            for i in range(1, len(cur)):
                name, content = cur[i].split("(")
                res[content].append((len(all_dirs), name))
            
            all_dirs.append(cur[0] + "/")
        
        res_list = []
        for k in res:
            if len(res[k]) > 1:
                res_list.append([])
                for id, name in res[k]:
                    res_list[-1].append(all_dirs[id] + name)
        
        return res_list
        

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]

print(Solution().findDuplicate(paths))       
        