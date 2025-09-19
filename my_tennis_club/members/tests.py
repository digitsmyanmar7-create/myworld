from django.test import TestCase

# Create your tests here.

class Person:
  def __init__(self, name, age,eye):
    self.name = name
    self.age = age
    self.eye = eye

  def __str__(self):
    return f"{self.name}({self.age}){self.eye}"

p1 = Person("John", 36,'blue')

print(p1)

