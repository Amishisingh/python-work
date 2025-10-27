class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.1427*self.radius*self.radius

class square:
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

shapes=(circle(8),square(8))

for shape in shapes:
    print("area:",shape.area())


