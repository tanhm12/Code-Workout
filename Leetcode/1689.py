
def minPartitions(n: str):
    maxx = "0"
    for i in n:
        if i == "9":
            return 9
        if i > maxx:
            maxx = i
    
    return int(maxx)


n = "32"
n = "27346209830709182346"
print(minPartitions(n))
