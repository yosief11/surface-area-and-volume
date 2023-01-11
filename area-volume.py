class Cube:

    def __init__(self, side):
        self.side = side

    def getSideLength(self):
        return self.side

    def surfaceArea(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3


def main():

    side = eval(input("Enter a side length: "))
    cube = Cube(side)
    area = cube.surfaceArea()
    vol = cube.volume()
    print("The Area is: {0:4.0f}".format(area))
    print("The Volume is: {0:4.0f}".format(vol))

main()
