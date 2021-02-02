# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        # calcular CSS-style HEX code
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red, self.green, self.blue
            )
        else:
            raise AttributeError

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        # call super so that __getattr__ is not called instead
        super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return("red", "green", "blue", "rgbcolor", "hexcolor")

def main():
    # create an instance of myColor
    cls1 = myColor()
    # TODO: print the value of a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: set the value of a computed attribute
    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: access a regular attribute (declared values)
    print(cls1.red)

    # TODO: list the available attributes (attributes that my object supports)
    print(dir(cls1))

if __name__ == "__main__":
    main()
