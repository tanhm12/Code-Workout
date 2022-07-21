from array import array


def pairs(k, arr):
    arr_set = set(arr)
    
   
    
    # def find_and_remove(item1, item2):
    #     if item2 in arr_set:
    #         # arr_set.remove(item1)
    #         # arr_set.remove(item2)
    #         return 1
    #     return 0
    
    res = 0
    for item in arr:
        if item in arr_set and (item + k) in arr_set:
            res += 1
            # if item < k:
            #     res += find_and_remove(item, item + k)
            
            # elif item > k:
            #     res += find_and_remove(item, item - k)
            
            # else:
            #     temp = find_and_remove(item, item + k)
            #     if temp == 1:
            #         res += temp
            #     else:
            #         res += find_and_remove(item, item - k)
    
    
    # minn = 0
    # maxx = int(2**31)
    # for i  in arr:
    #     if i < minn:
    #         minn = i
    #     if i > maxx:
    #         maxx = i
    
    # def find_and_remove_all(item):
    #     res = 0
    #     left = item
    #     while True:
    #         left = left - k
    #         if left in arr_set:
    #             arr_set.remove(left)
    #             res += 1
    #         if left <= minn:
    #             break

    
    return res


arr = [1, 5, 3, 4, 2]
k = 2
print(pairs(k, arr))
            
