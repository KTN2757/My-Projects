class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False


p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)
