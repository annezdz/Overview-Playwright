"""
sets attributes for an object at object creation _ is a constructor.
__init__ methos is not required BUT is generally used to set
default state of object when it is created
The __init__ method is the first method for a
self - instance of a class
self reference variable - used to reference the object that is constructed by
 the init method
"""
import random


class Person:

    def __init__(self, first_name, last_name, health, status):
        """ initialize attributes to be used in/available for all \
        class methods in this class, and for class objects created \
        by this class"""

        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.status = status

    def introduce(self):
        """All people introduce themselves"""
        print('Hello, my name is {} {}'.format(self.first_name, self.last_name))

    def emote(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print(f'{self.first_name} is happy today')
        elif emotion == 2:
            print(f'{self.first_name} is sad today')

    def status_change(self):
        if self.health == 100:
            print(f'{self.first_name} is totally healthy')
        elif self.health <= 76:
            print(f'{self.first_name} feels unwell')
        elif self.health <= 50:
            print(f'{self.first_name} goes to doctor')
        else:
            print(f'{self.first_name} is unconscious')


Maria = Person('Maria', 'Gutierrez', 95, status=True)
Rey = Person('Rey', 'Jones', 88, status=False)
Lee = Person('Lee', 'Williams', 72, status=True)

print(f'{Maria.first_name} is my friend ? {Maria.status}')
print(f'{Rey.first_name} is my friend ? {Rey.status}')

Maria.introduce()
Rey.introduce()
Lee.introduce()
Rey.emote()
Rey.status_change()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print(f'{other.first_name}, you are tired and weak')

    def steal(self, other):
        print(f'ha ha ha, {other.first_name}, I have your stuff!')
        if other.status:
            other.status = False

    def introduce(self):
        print('Youre my mortal enemy')


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.introduce()

