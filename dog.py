class Dog(object):
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def bark(self):
      return 'Woof woof!'

dog = Dog('Sparky', 7)
print dog.name
print dog.age
print dog.bark()
