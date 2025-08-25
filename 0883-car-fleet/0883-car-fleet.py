class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_ds = []
        n = len(position)
        for i in range(0,n):
            cars_ds.append((position[i],speed[i]))
        # sort the groups based on position
        cars_ds.sort(key = lambda x:x[0],reverse=True)

        fleets = 1
        prevTime = (target - cars_ds[0][0]) / cars_ds[0][1]
        for i in range(1,len(cars_ds)):
            currCar = cars_ds[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets+=1
                prevTime = currTime
        return fleets