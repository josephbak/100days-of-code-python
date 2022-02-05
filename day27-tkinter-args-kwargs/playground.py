
def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make= "Nissan")
print(my_car.model)