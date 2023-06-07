class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType-1] == 0:
            return False
        self.slots[carType-1] -= 1
        return True


parkingSystem = ParkingSystem(1, 1, 0)
parkingSystem.addCar(1)  # return true because there is 1 available slot for a big car
parkingSystem.addCar(2)  # return true because there is 1 available slot for a medium car
parkingSystem.addCar(3)  # return false because there is no available slot for a small car
parkingSystem.addCar(1)  # return false because there is no available slot for a big car. It is already occupied.