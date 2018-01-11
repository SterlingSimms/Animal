class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health
        return self
Animal1 = Animal("Human", 300)
Animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
Dog1 = Dog("Dog", 150)
Dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(Animal):
        print "I am a Dragon"
Dragon1 = Dragon("Dragon", 170)
Dragon1.walk().walk().fly().fly().display_health()

class Cat(Animal):
    def __init__(self, name, health):
        super(Cat, self).__init__(name, health)
        self.health = 200
Cat1 = Cat("Cat", 200)
Cat1.walk().walk().run().display_health().fly()

