class SmallestInfiniteSet:
	def __init__(self):
		from queue import PriorityQueue
		self.data = PriorityQueue()
		self.pointer = 1

	def popSmallest(self) -> int:
		if not self.data.empty():
			res = self.data.get()
			while not self.data.empty() and res ==  self.data.queue[0]:
				self.data.get()
			return res
		self.pointer += 1
		return self.pointer - 1

	def addBack(self, num: int) -> None:
		if num < self.pointer:
			self.data.put(num)