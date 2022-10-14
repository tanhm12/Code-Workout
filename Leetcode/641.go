type MyCircularDeque struct {
	First, Last int
	Queue       []interface{}
}

func Constructor(maxSize int) MyCircularDeque {
	return MyCircularDeque{First: 0, Last: 0, Queue: make([]interface{}, maxSize)}
}

func (this *MyCircularDeque) IsFull() bool {
	if this.Queue[this.First] != nil && this.Last == this.First {
		return true
	}
	return false
}

func (this *MyCircularDeque) IsEmpty() bool {
	if this.Queue[this.First] == nil && this.Last == this.First {
		return true
	}
	return false
}

func (this *MyCircularDeque) Size() int {
	if this.Last < this.First {
		return this.Last + len(this.Queue) - this.First
	} else {
		return this.Last - this.First
	}
}

func (this *MyCircularDeque) InsertLast(val interface{}) bool {
	if !this.IsFull() {
		this.Queue[this.Last] = val
		this.Last++
		if this.Last == len(this.Queue) {
			this.Last = 0
		}
		return true
	} else {
		return false
	}
}

func (this *MyCircularDeque) InsertFront(val interface{}) bool {
	if !this.IsFull() {
		this.First--
		if this.First < 0 {
			this.First += len(this.Queue)
		}
		this.Queue[this.First] = val
		return true
	} else {
		return false
	}
}

func (this *MyCircularDeque) DeleteLast() bool {
	if !this.IsEmpty() {
		this.Last--
		if this.Last < 0 {
			this.Last += len(this.Queue)
		}
		this.Queue[this.Last] = nil
		return true
	} else {
		return false
	}
}

func (this *MyCircularDeque) DeleteFront() bool {
	if !this.IsEmpty() {
		this.Queue[this.First] = nil
		this.First++
		if this.First == len(this.Queue) {
			this.First = 0
		}

		return true
	} else {
		return false
	}
}

func (this *MyCircularDeque) GetFront() interface{} {
	if !this.IsEmpty() {
		return this.Queue[this.First]
	} else {
		return -1
	}
}

func (this *MyCircularDeque) GetRear() interface{} {
	if !this.IsEmpty() {
		if this.Last == 0 {
			return this.Queue[len(this.Queue)-1]
		}
		return this.Queue[this.Last-1]
	} else {
		return -1
	}
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */