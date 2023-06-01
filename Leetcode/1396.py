from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.customer = defaultdict(lambda :["", 0])
        self.info = defaultdict(lambda: defaultdict(lambda : {"sum": 0, "n": 0}))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStationName, start_time = self.customer[id]
        self.info[startStationName][stationName]["sum"] += t - start_time
        self.info[startStationName][stationName]["n"] += 1
        del self.customer[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.info[startStation][endStation]["sum"] / self.info[startStation][endStation]["n"] 


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)