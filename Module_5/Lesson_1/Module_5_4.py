class Buiding:
    total = 0
    def __init__(self):
        Buiding.total += 1
buidings = [Buiding() for _ in range(40)]
print(Buiding.total)