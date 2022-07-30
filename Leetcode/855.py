from collections import defaultdict
class ExamRoom:
    
    def __init__(self, n: int):
        
        from sortedcontainers import SortedList
        self.n = n
        self.current_seats = SortedList()
        self.distances = []
        self.unique_distances = defaultdict(int)

    def seat(self):
        if len(self.current_seats) == 0:
            self.current_seats.add(0)
            self.distances = [0, self.n-1]
            self.unique_distances = defaultdict(int)
            self.unique_distances[self.n-1] = 1
            return 0
        elif len(self.current_seats) == 1:
            if self.distances[0] >= self.distances[1]:
                self.current_seats.add(0)
                self.distances = [0, self.distances[0], self.distances[1]]
                return 0
            else:
                self.current_seats.add(self.n-1)
                self.distances = [self.distances[0], self.distances[1], 0]
                return self.n-1
        else:
            max_dis = max(self.unique_distances)
            # print(self.unique_distances, self.distances)
            mark = None
            if self.distances[0] >= max_dis//2:
                if self.distances[0] >= self.distances[-1]:
                    self.distances = [0] + self.distances
                    self.current_seats.add(0)
                    return 0
                else:
                    self.distances = self.distances + [0]
                    self.current_seats.add(self.n-1)
                    return self.n-1
            elif self.distances[-1] > max_dis//2:
                self.distances = self.distances + [0]
                self.current_seats.add(self.n-1)
                return self.n-1
                    
            # elif max_dis == 1:
            #     if self.distances[0] == 0:
            #         self.current_seats.add(self.n-1)
            #         self.distances.append(0)
            #         return self.n-1
            #     else:
            #         self.current_seats.add(0)
            #         self.distances = [0] + self.distances
            #         return 0
            # elif max_dis == 2:
            #     if self.distances[0] != 0:
            #         self.current_seats.add(0)
            #         self.distances = [0] + self.distances
            #         return 0
            #     else:
            #         mark = None
            #         for i in range(len(self.distances)):
            #             if self.distances[i] == 2:
            #                 mark = i
            #                 break
            #         self.unique_distances[2] -= 1
            #         if self.unique_distances[2] == 0:
            #             del self.unique_distances[2]
                        
            #         self.distances.insert(mark + 1, 1)
            #         self.distances[mark] = 1
            #         res = None
            #         if mark == 0:
            #             res = self.distances[mark]
            #         else:
            #             res = self.current_seats[mark-1] + self.distances[mark]
            #         self.current_seats.add(res)
            #         # print(res, mark, self.current_seats, self.distances)
            #         return res
                            
                            
            elif max_dis % 2 == 0:
                for i in range(len(self.distances)):
                    dis = self.distances[i]
                    if dis == max_dis:
                        mark = i
                        break
            else:
                max_dis1 = max_dis - 1
                for i in range(len(self.distances)):
                    dis = self.distances[i]
                    if dis == max_dis or dis == max_dis1:
                        mark = i
                        break
            
            new = self.distances[mark] // 2
            self.unique_distances[self.distances[mark]] -= 1
            if self.unique_distances[self.distances[mark]] == 0:
                del self.unique_distances[self.distances[mark]]
            
            self.distances.insert(mark + 1, self.distances[mark]-new)
            self.distances[mark] = new
            
            self.unique_distances[self.distances[mark]] += 1
            self.unique_distances[self.distances[mark+1]] += 1
            
            
            res = None
            if mark == 0:
                res = self.distances[mark]
            else:
                res = self.current_seats[mark-1] + self.distances[mark]
            self.current_seats.add(res)
            # print(res, mark, self.current_seats, self.distances, self.unique_distances)
            return res
                    

    def leave(self, p: int):
        # print(p, self.distances, self.unique_distances)
        id = self.current_seats.bisect_left(p)
        self.current_seats.remove(p)
        
        for i in (id, id + 1):
            self.unique_distances[self.distances[i]] -= 1
            if self.unique_distances[self.distances[i]] == 0:
                del self.unique_distances[self.distances[i]]
            
        new = self.distances[id] + self.distances[id + 1]
        self.distances[id] = new
        self.distances.pop(id + 1)
        self.unique_distances[self.distances[id]] += 1
        
        # print(self.distances, self.unique_distances)

        
# inputs = [[11], [], [], [], [], [], [], [], [5], [10], []]
inputs = [[10],[],[],[],[0],[4],[],[],[],[],[],[],[],[],[],[0],[4],[],[],[7],[],[3],[],[3],[],[9],[],[0],[8],[],[],[0],[8],[],[],[2]]
# inputs = [[8],[],[],[],[0],[7],[],[],[],[],[],[],[]]
# inputs = [[9],[],[],[],[],[4],[],[],[],[],[],[],[3],[]]

room = ExamRoom(inputs[0][0])


res = [None]
for i in range(1, len(inputs)):
    t = None
    if len(inputs[i]) == 0:
        t = room.seat()
    else:
        room.leave(inputs[i][0])
    res.append(t)
    
print(res)
        