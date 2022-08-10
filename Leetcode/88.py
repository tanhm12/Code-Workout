def marge(nums1, m, nums2, n):
    p1, p2 = m-1, n-1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] <= nums2[p2]:
            nums1[p1+p2+1] = nums2[p2]
            p2 -= 1
        else:
            nums1[p1+p2+1] = nums1[p1]
            p1 -= 1
            
    if p1 < 0:
        while p2 >=0:
            nums1[p2] = nums2[p2]
            p2 -= 1
    