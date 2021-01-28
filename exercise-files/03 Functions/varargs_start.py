# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # TODO: pass different arguments
    print(addition(5, 10, 15, 20))
    print(addition(5, 10, 15, 20))

    # TODO: pass an existing list
    myNums = [5,10,15,20]
    # the star operator here acts like a spread operator
    print(addition(*myNums))

if __name__ == "__main__":
    main()
