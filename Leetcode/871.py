from typing import List

def minRefuelStops( target: int, startFuel: int, stations: List[List[int]]):
    
    if startFuel >= target:
        return 0
    MAX_FUEL = int(1e9)
    
    import bisect
    from queue import PriorityQueue
    
    qstations = PriorityQueue()
    # qstations.put([-startFuel, 0])
    
    res = 0
    current_fuel = startFuel
        
    for i in range(len(stations)):
        pos, fuel = stations[i]
        cur_target = min(target, pos)
        
        while current_fuel < cur_target and not qstations.empty():
            # print(qstations.queue[0])
            current_fuel -= qstations.get()[0]
            res += 1
            if current_fuel >= cur_target:
                break
        
        # print(i, stations[i], cur_target, current_fuel,  res)
        
        if cur_target >= target:
            return res
        elif current_fuel < cur_target:
            return -1
        else:
            qstations.put([-fuel, pos])
    
    if current_fuel >= target:
        return res
           
    while current_fuel < target and not qstations.empty():
        current_fuel -= qstations.get()[0]
        res += 1
        if current_fuel >= target:
            return res
    
    
    return -1

                    
                    
        
target = 1
startFuel = 1
stations = []

# target = 100
# startFuel = 1
# stations = [[10,100]]

# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]

# target = 999
# startFuel = 1000
# stations = [[5,100],[997,100],[998,100]]

# target = 100
# startFuel = 25
# stations = [[25,25],[50,25],[75,25]]

# target = 1000
# startFuel = 299
# stations = [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]

print(minRefuelStops(target, startFuel, stations))
