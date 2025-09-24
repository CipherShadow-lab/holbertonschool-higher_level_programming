#!/usr/bin/python3

class SwimMixin:
    """Mixin class to add swimming ability."""

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin class to add flying ability."""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits swimming and flying abilities."""

    def roar(self):
        print("The dragon roars!")

if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
