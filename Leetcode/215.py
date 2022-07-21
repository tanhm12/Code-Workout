from typing import List

def findKthLargest(nums: List[int], k: int):
    def heapify(arr, i):
        arr_len = len(arr)
        largest = i
        left_child = 2*i + 1
        rigth_child = 2*i + 2
        
        if left_child < arr_len and arr[left_child] > arr[largest]:
            largest = left_child
        
        if rigth_child < arr_len and arr[rigth_child] > arr[largest]:
            largest = rigth_child
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, largest)
    
    def build_heap(arr):
        for i in range(len(arr)-1, -1,  -1) :
            heapify(arr, i)
    
    
    build_heap(nums)
    
    from queue import PriorityQueue
    pq = PriorityQueue(len(nums))
    
    pq.queue = [-1 * item for item in nums]
    for i in range(k-1):
        pq.get()
        
    return -1 * pq.get()


def findKthLargest(nums: List[int], k: int):
        
    return sorted(nums, reverse=True)[k-1]


print(findKthLargest(nums = [3,2,1,5,6,4], k = 2))
