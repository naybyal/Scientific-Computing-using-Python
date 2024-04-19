
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Mammal sound"

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Bird sound"


class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Bat sound"


bat = Bat("Hermano")

print(bat.speak())
print(bat.name)

