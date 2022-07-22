def getDistances(arr):
    from collections import defaultdict
    
    all_pos = defaultdict(list)
    for i, item in enumerate(arr):
        all_pos[item].append(i)
        
    
    accu_sum = {}
    for item in all_pos:
        accu_sum_item = [all_pos[item][0]] * len(all_pos[item])
        for i in range(1, len(all_pos[item])):
            accu_sum_item[i] = accu_sum_item[i-1] + all_pos[item][i]

        accu_sum[item] = accu_sum_item
    
    import bisect
    res = [0] * len(arr)
    
    for i, item in enumerate(arr):
        unique_pos = bisect.bisect_left(all_pos[item], i)
        # print(i, all_pos[item], unique_pos)
        pref_sum = i * (unique_pos + 1) - accu_sum[item][unique_pos]
        suf_sum = accu_sum[item][-1] - accu_sum[item][unique_pos] - i*(len(accu_sum[item]) - unique_pos-1)
        # print(pref_sum, suf_sum)
        res[i] = pref_sum + suf_sum
        
    return res


arr = [2,1,3,1,2,3,3]
print(getDistances(arr))

    