class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x = self.x + 1
        self.z = self.z + 1

    def incrementaZ(self):
        self.z = self.z + 1

class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y = self.y + 1
        self.z = self.z + 1

    def incrementaZ(self):
        self.z = self.z + 1

class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)

    def incrementaXYZ(self):
        self.x = self.x + 1
        self.y = self.y + 1
        self.z = self.z + 1

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

class Main:

        d = D(1, 2, 3)
        print(d)

        d.incrementaXYZ()
        print(d)

        d.incrementaXZ()
        print(d)

        d.incrementaYZ()
        print(d)

        d.incrementaZ()
        print(d)

