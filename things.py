class Thing:
    def __init__(self, x=0, y=0, weight=0.0):
        self.x = x
        self.y = y
        self.weight = weight

    def __str__(self):
        return "{:>6.2f}kg at ({:2d},{:>3d})".format(self.weight,self.x,self.y)


a = Thing(10, 5, 17.2)
b = Thing(3, 2, 120)
c = Thing(14, 12, 1.95)

things = [a, b, c]

for thing in things:
    print(thing)
