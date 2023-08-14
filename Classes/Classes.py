class Point:

    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y


class DefaultPoint:

    # X and Y values just set to some default values
    def __init__(self):
        self.x = 10
        self.y = 10


if __name__ == "__main__":
    pt = Point(3, 4)
    print(pt.x, pt.y)

    pt_def = DefaultPoint()
    print(pt_def.x, pt_def.y)

    pt_def.x = 5
    pt_def.y = 5

    print(pt_def.x, pt_def.y)
