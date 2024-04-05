def __init__ (self, name, number):
    self.name = name
    self._scores = []

    for count in range(number):
        self._scores.append(0)