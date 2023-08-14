class Point(object):

    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
        print('Point::__init__()')

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def info(self):
        print(f'Point({self.x}, {self.y})')


class Point3D(Point):

    def __init__(self, coord_x, coord_y, coord_z):
        super().__init__(coord_x, coord_y)
        self.z = coord_z
        print('Point3D::__init__()')

    def __repr__(self):
        return f'Point3D({self.x}, {self.y}, {self.z})'

    def info(self):
        print( f'Point3D({self.x}, {self.y}, {self.z})')


if __name__ == "__main__":
    pt = Point3D(1, 2, 3)
    pt.info()