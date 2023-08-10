class Point:

    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y


if __name__ == "__main__":
    pt = Point(3, 4)
    print(pt.x, pt.y)
