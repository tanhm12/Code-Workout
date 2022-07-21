from typing import List

def maximumUnits(boxTypes: List[List[int]], truckSize: int):
    boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
    print(boxTypes)
    
    res = 0
    for num_boxes, box_size in  boxTypes:
        # print(res, num_boxes, box_size)
        if num_boxes >= truckSize:
            res += box_size * truckSize
            break
        else:
            truckSize -= num_boxes
            res += box_size * num_boxes
    
    return res
    

print(maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))
    