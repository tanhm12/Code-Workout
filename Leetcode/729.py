import bisect

class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int):
        start_pos = bisect.bisect(self.calendar, start)
        end_pos = bisect.bisect_left(self.calendar, end)
        
        if start_pos == end_pos and start_pos % 2 == 0:
            self.calendar.insert(end_pos, end)
            self.calendar.insert(start_pos, start)
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:

# inputs = [[], [10, 20], [15, 25], [20, 30]]
inputs = [[],[20,29],[13,22],[44,50],[1,7],[2,10],[14,20],[19,25],[36,42],[45,50],[47,50],[39,45],[44,50],[16,25],[45,50],[45,50],[12,20],[21,29],[11,20],[12,17],[34,40],[10,18],[38,44],[23,32],[38,44],[15,20],[27,33],[34,42],[44,50],[35,40],[24,31]]
obj = MyCalendar()
for start, end in inputs[1:]:
    print(start, end, obj.book(start,end), obj.calendar)