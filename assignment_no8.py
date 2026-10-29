class Father:
    def house(self):
        print("father has a house")
class Son(Father):
    def bike(self):
        print("son has a bike")
s = Son()
s.house()
s.bike()




class Father:
    def show1(self):
        print("this is father")
class Mother:
    def show2(self):
        print("this is mother")
class Child(Father, Mother):
    def show3(self):
        print("this is child")
c = Child()
c.show1()
c.show2()
c.show3()



class Person:
    def show(self):
        print("person details")
class Student(Person):
    def study(self):
        print("student is studying")
class Monitor(Student):
    def duty(self):
        print("monitor is doing duty")
m = Monitor()
m.show()
m.study()
m.duty()


class Animal:
    def eat(self):
        print("animal eats food")
class Dog(Animal):
    def bark(self):
        print("dog barks")
class Cat(Animal):
    def sound(self):
        print("cat meows")
d = Dog()
c = Cat()
d.eat()
d.bark()
c.eat()
c.sound()


class Person:
    def show(self):
        print("person details")
class Student(Person):
    def study(self):
        print("student studies")
class Employee(Person):
    def work(self):
        print("employee works")
class Intern(Student, Employee):
    def display(self):
        print("intern works and studies")
i = Intern()
i.show()
i.study()
i.work()
i.display()


class Calculator:
    def add(self, a, b=0, c=0):
        print(a + b + c)
c = Calculator()
c.add(10, 20)
c.add(10, 20, 30)
c.add(10)



class Animal:
    def sound(self):
        print("animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
class Cat(Animal):
    def sound(self):
        print("cat meows")
a = Animal()
d = Dog()
c = Cat()
a.sound()
d.sound()
c.sound()


class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)