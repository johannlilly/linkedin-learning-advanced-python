# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10,20)
    p2 = Point(30,40)
    print(p1, p2)
    # use descriptive names to access the data
    print(p1.x, p2.y)

    # TODO: use _replace to create a new instance (a helper function)
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == "__main__":
    main()
