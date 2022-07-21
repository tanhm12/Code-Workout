from typing import List


# def furthestBuilding(heights: List[int], bricks: int, ladders: int):
#     delta_heights = [heights[0]]
#     cumulative_delta_heights = [delta_heights[0]]
#     for i in range(1, len(heights)):
#         delta_heights.append(max(heights[i] - heights[i-1], 0))
#         cumulative_delta_heights.append(cumulative_delta_heights[-1] + delta_heights[-1])
        
    
#     if ladders == 0:
#         for i in range(len(cumulative_delta_heights)):
#             if cumulative_delta_heights[i] > bricks:
#                 return i + 1
#         return len(cumulative_delta_heights) + 1
    
    
#     min_heap = [-1] * ladders
#     heap_length = len(min_heap)
    
#     def add_to_heap(val, heap=min_heap):
#         return_val = heap[0]
#         if val < return_val:
#             return val
        
        
#         # cur_node = len(heap) - 1  # leaf
#         # heap[0] = heap[cur_node]
#         # heap[cur_node] = val
        
#         # while True:
#         #     parent_node = (cur_node-1) // 2
#         #     if parent_node >= cur_node:
#         #         break
            
#         #     if heap[parent_node] < heap[cur_node]:
#         #         heap[parent_node], heap[cur_node] = heap[cur_node], heap[parent_node]
#         #     else:
#         #         break
#         #     cur_node = parent_node
        
#         cur_node = 0  # leaf
#         heap[0] = val
        
#         while True:
#             left_child_node = 2 * cur_node + 1
#             right_child_node = 2 * cur_node + 2
            
#             if left_child_node >= heap_length:
#                 break
            
                
            
#         return return_val
    
    
#     prev = 0
#     for i in range(len(delta_heights)):
#         val = delta_heights[i]
#         prev = i
#         if val == 0:
#             continue
#         add_to_heap(val)
#         if min_heap[0] != -1:
#             break
    
#     if prev == len(heights) - 1:
#         return prev + 1

#     print(min_heap)
    
#     for i in range(prev+1, len(delta_heights)):
#         val = delta_heights[i]
#         if val == 0:
#             continue
        
#         bricks_needed = add_to_heap(val)
#         print(i, val, bricks_needed, min_heap)
#         bricks = bricks - bricks_needed
        
#         if bricks < 0:
#             return i + 1
        
#     return len(heights)



def furthestBuilding(heights: List[int], bricks: int, ladders: int):
    if len(heights) == 1:
        return 0
    
    delta_heights = [heights[1]-heights[0]]
    for i in range(2, len(heights)):
        delta_heights.append(max(heights[i] - heights[i-1], 0))
    
    if ladders == 0:
        for i in range(len(delta_heights)):
            bricks -=  delta_heights[i]
            if bricks < 0:
                return i
            
        return len(delta_heights)
    
    
    from queue import PriorityQueue
    min_heap = PriorityQueue(ladders)
    
    
    prev = 0
    for i in range(len(delta_heights)):
        val = delta_heights[i]
        prev = i
        if val == 0:
            continue
        min_heap.put(val)
        if min_heap.full():
            break
    
    if prev == len(heights) - 1:
        return prev + 1

    # print(min_heap.queue)
    
    for i in range(prev+1, len(delta_heights)):
        val = delta_heights[i]
        if val == 0:
            continue
        
        if val > min_heap.queue[0]:   
            bricks_needed = min_heap.get()
            min_heap.put(val)
        else:
            bricks_needed =  val
        # print(i, bricks, bricks_needed, min_heap.queue)
        bricks = bricks - bricks_needed
        
        if bricks < 0:
            return i 
        
    return len(heights)-1


# print(furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
# print(furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
# print(furthestBuilding(heights = [14,3, 19, 3], bricks = 17, ladders = 0))
# print(furthestBuilding(heights = [14,3, 19], bricks = 17, ladders = 0))
# print(furthestBuilding(heights = [1, 2], bricks = 0, ladders = 0))
