class Point:

    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def move_right(self, step):
        self.x += step

    def move_up(self, step):
        self. y += step


if __name__ == "__main__":
    pt = Point(3, 4)
    print(pt.x, pt.y)

    pt.move_right(2)
    print(pt.x, pt.y)

    pt.move_up(1)
    print(pt.x, pt.y)
