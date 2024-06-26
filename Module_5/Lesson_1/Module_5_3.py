class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        if not isinstance(other, Building):
            return NotImplemented
        return (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType)
building1 = Building(10, 'Office')
building2 = Building(10, 'Office')
building3 = Building(6, 'Residental')
print(building1 == building2)
print(building1 == building3)
