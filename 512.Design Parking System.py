# Design Parking System

# Time Complexity - O(1) || Space Complexity - O(1)

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [0,big,medium,small] 

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] > 0:
            self.parking[carType]-=1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
