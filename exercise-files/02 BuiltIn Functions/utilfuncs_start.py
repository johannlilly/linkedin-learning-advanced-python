# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    tuple1 = {1, 2, 3, 0, 5, 6}
    
    # TODO: any will return true if any of the sequence values are true
    print(any(list1))
    print(any(tuple1))

    # TODO: all will return true only if all values are true
    print(all(list1))
    print(all(tuple1))

    # TODO: min and max will return minimum and maximum values in a sequence
    print(min(list1))
    print(max(list1))
    print(min(tuple1))
    print(max(tuple1))

    # TODO: Use sum() to sum up all of the values in a sequence
    print(sum(list1))
    print(sum(tuple1))
    
if __name__ == "__main__":
    main()
    