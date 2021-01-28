# Demonstrate the use of keyword-only arguments
'''
you can separate positional arguments from arguments
which are keyword-only using an asterisk
'''

# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, suppressExceptions=False):
    pass


def main():
    # try to call the function without the keyword
    myFunction(1, 2, True)
    # use the keyword
    myFunction(1, 2, suppressExceptions=True)


if __name__ == "__main__":
    main()
