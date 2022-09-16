package main

type SnapshotArray struct {
	Length int
	Arr    [][][]int
	SnapId int
}

func Constructor(length int) SnapshotArray {
	arr := make([][][]int, length)
	snapId := -1
	for i := 0; i < length; i++ {
		arr[i] = make([][]int, 1)
		arr[i][0] = []int{-1, 0}
	}
	return SnapshotArray{
		Length: length,
		Arr:    arr,
		SnapId: snapId,
	}
}

func (self *SnapshotArray) Set(index int, val int) {
	if self.Arr[index][len(self.Arr[index])-1][0] == self.SnapId {
		self.Arr[index][len(self.Arr[index])-1][1] = val
	} else {
		self.Arr[index] = append(self.Arr[index], []int{self.SnapId, val})
	}
}

func (self *SnapshotArray) Snap() int {
	self.SnapId++
	return self.SnapId
}

func (self *SnapshotArray) Get(index int, snap_id int) int {
	snap_id--
	l := 0
	r := len(self.Arr[index]) - 1
	var m int
	for l < r {
		m = (l + r) / 2
		if self.Arr[index][m][0] <= snap_id {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	if self.Arr[index][l][0] > snap_id {
		l--
	}
	return self.Arr[index][l][1]
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := Constructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */
