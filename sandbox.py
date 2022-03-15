import math
import random


class Cat:
    happiness = math.comb(5, 2)

    def say_meow(self):
        print("meow")

    def eat(self):
        self.happiness += random.randint(5, 20)


cat = Cat()
cat.say_meow()
cat.eat()
