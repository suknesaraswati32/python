class Student:
    name = "saraswati"
    age = 20
    def display(self):
        print(self.name)
        print(self.age)
s1 = Student()
s1.display()



class Student:
    def display(self):
        print("hello student")
s1 = Student()
s2 = Student()
s1.display()
s2.display()



class Student:
    def __init__(self):
        self.__marks = 90
    def display(self):
        print("marks:", self.__marks)
s1 = Student()
s1.display()



class Person:
    def display(self):
        print("this is a person")
class Student(Person):
    def show(self):
        print("this is a student")
s1 = Student()
s1.display()
s1.show()



class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("meow")
d = Dog()
c = Cat()
d.sound()
c.sound()


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("bark")
d = Dog()
d.sound()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
s1 = Student("saraswati", 20)
s1.display()


class Student:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("object destroyed")
s1 = Student()
del s1