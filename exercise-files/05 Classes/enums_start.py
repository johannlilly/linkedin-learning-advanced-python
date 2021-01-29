# define enumerations using the Enum base class
"""
Advanced Classes and Objects: Defining enumerations
- Duplicate names (keys) are not allowed
- Duplicate values *are* allowed,
  unless using the `unique` decorator, applied to the class
- the `auto` function automatically assigns values to enums
- you can use enums as hash values
"""

from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

def main():
    pass
    # TODO: enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE)) # class type
    print(repr(Fruit.APPLE)) # string containing a printable representation of an object

    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # TODO: print the auto-generated value
    print(Fruit.PEAR.value)

    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "GME diamond hands"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
