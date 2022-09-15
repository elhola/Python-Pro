class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'x= {self.x}, y= {self.y}, z= {self.z}'

    def volume(self):
        v = self.x * self.y * self.z
        return v

    @staticmethod
    def sum_volume(vol1, vol2):
        vol1 = Box.volume(vol1)
        vol2 = Box.volume(vol2)
        return vol1 + vol2


box1 = Box(1, 2, 3)
box2 = Box(4, 5, 6)

print(Box.sum_volume(box2, box1))
