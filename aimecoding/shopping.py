b,n,m = list(map(int, input().split()))
jap_toys  = list(map(int, input().split()))
american_toys  = list(map(int, input().split()))

##############################sol1#####################
# import bisect
# american_toys.sort()

# res = -1

# for jp in jap_toys:
#     if jp <= b:
#         max_pos = bisect.bisect_left(american_toys, b - jp)
#         # print(max_pos, b - jp)
#         if 0<=max_pos<len(american_toys) and jp + american_toys[max_pos] <= b:
#             res = max(res, jp + american_toys[max_pos])
#         if 0<=max_pos-1<len(american_toys) and jp + american_toys[max_pos-1] <= b:
#             res = max(res, jp + american_toys[max_pos-1])
# print(res)


##############################sol2#####################
american_toys.sort()
jap_toys.sort()

res = -1
us_toy_id = len(american_toys) - 1
for ja_toy in jap_toys:
    if ja_toy < b:
        while ja_toy + american_toys[us_toy_id] > b and us_toy_id >= 0:
            us_toy_id -= 1
        if us_toy_id == -1:
            break
        res = max(res, ja_toy + american_toys[us_toy_id])
    
print(res)
