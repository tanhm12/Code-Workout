
class Solution:
    def pushDominoes(self, dominoes: str):
        res = []
        i = 0
        while i < len(dominoes):
            next_i = i
            if dominoes[i] == "." or dominoes[i] == "L":
                for j in range(i+1, len(dominoes)):
                    if dominoes[j] == "L":
                        res.extend(["L"] * (j-i+1))
                        next_i = j+1
                        break
                    elif dominoes[j] == "R":
                        next_i = j
                        res.extend(dominoes[i:j])
                        break
            elif dominoes[i] == "R":
                next_i = i
                for j in range(i+1, len(dominoes)):
                    if dominoes[j] == "L":
                        middle = (j+i) // 2
                        res.extend(["R"] * (middle + 1-i) + ["L"] * (j-middle))
                        if  (j-i) % 2 == 0:
                            res[middle] = "."
                        next_i = j+1
                        break
                    elif dominoes[j] == "R":
                        next_i = j 
                        res.extend(["R"] * (j-i))
                        break
            if next_i == i:
                if dominoes[i] == "R":
                    res.extend(["R"] * (len(dominoes)-i))
                else:
                    res.extend(list(dominoes[i:]))
                break
            i = next_i
        return ''.join(res)
    
    
dominoes = ".L.R...LR..L.."
dominoes = "RR.L"
dominoes = ".L.R...L..L.R..R..L.."
dominoes = ".L.R."

print(dominoes)
print(Solution().pushDominoes(dominoes))
                        