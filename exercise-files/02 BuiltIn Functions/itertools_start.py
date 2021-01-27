# advanced iteration functions in the itertools package

import itertools

def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))


    # TODO: use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals)
    print(list(acc))
    # find the biggest number so far
    acc = itertools.accumulate(vals, max)
    print(list(acc))
            
    # TODO: use chain to connect sequences together
    # almost like prototype.split and concatenate in JavaScript
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them; like a threshold
    # dropwhile(): skip values while testFunction() returns true, then return every value after that
    print(list(itertools.dropwhile(testFunction, vals)))
    # takewhile(): return values from sequence while testFunction() returns true, then stop
    print(list(itertools.takewhile(testFunction, vals)))
    
    
if __name__ == "__main__":
    main()
    