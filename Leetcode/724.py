def pivotIndex(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i, item in enumerate(nums):
        prefix_sum[i+1] = prefix_sum[i] + item
        
    
    for i, item in enumerate(nums):
        if prefix_sum[i] == prefix_sum[-1] - prefix_sum[i+1]:
            return i
    
    return -1

nums = [1,7,3,6,5,6]
nums = [1,2,3]
nums = [2,1,-1]
print(pivotIndex(nums))
    