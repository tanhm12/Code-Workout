class SnapshotArray:
    def __init__(self, length: int):
        self.length = length
        self.arr = [[[-1, 0]] for i in range(self.length)]
        self.snap_id = -1

    def set(self, index: int, val: int):
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int):
        snap_id  -= 1
        l = 0
        r = len(self.arr[index]) - 1
        while l < r:
            m = (l+r) // 2
            if self.arr[index][m][0] <= snap_id:
                l = m+1
            else:
                r = m-1
        
        if self.arr[index][l][0] > snap_id:
            l -= 1
        return self.arr[index][l][1]