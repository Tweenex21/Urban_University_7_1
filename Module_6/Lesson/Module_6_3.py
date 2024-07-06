class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"
    def run(self, dx):
        self.x_distance += dx
class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = "Я тренеруюсь, ем, сплю и повторяю"
    def fly(self, dy):
        self.y_distance += dy
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)
    def more(self, dx, dy):
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)
    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.more(10, 15)
print(p1.get_pos())
p1.more(-5, 20)
print(p1.get_pos())

p1.voice()
