class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNberOffloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)
My_house = House()
My_house.setNewNberOffloors(5)