def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(4, 5, 6, 3, 8))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=9, multiply=10)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GTR")
print(my_car.model)

