from typing import List

def scheduleCourse(courses: List[List[int]]):
    from functools import cmp_to_key
    
    def compare_course(c1, c2):
        if c1[0] == c2[0]:
            return c1[1] - c2[1]
        else:
            return c1[0] - c2[0]
    
    
    courses = [item for item in courses if item[1] >= item[0]]
    # courses = sorted(courses, key=cmp_to_key(compare_course))
    courses = sorted(courses, key=lambda x: x[1])
    # print(courses)

    if len(courses) == 0: 
        return 0
    
    from queue import PriorityQueue
    max_pq = PriorityQueue(len(courses))
    total_duration = 0
    
    for i in range(len(courses)):
        duration, end_time = courses[i]
        # if len(max_pq.queue) > 0 and duration >= -max_pq.queue[0] and end_time == current_endtime:
        #     continue
        # current_endtime = end_time
        
        max_pq.put(-duration)
        total_duration += duration
        if total_duration > end_time:
            current_max_duration = -max_pq.get()
            total_duration -= current_max_duration
            # max_pq.put(-1 * duration)
            # total_duration += duration - current_max_duration
        
    # print(max_pq.queue)
    return len(max_pq.queue)
    
    
print(scheduleCourse(courses = [[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]))            
        
    
        