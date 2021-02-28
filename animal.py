class Animal:
  def __init__(self, kind, name, age):
# initialize
    self.kind = kind
    self.name = name
    self.age = age 
# intance method
  def speak(self):

    return f'I am a {self.kind}, My name is {self.name} and I am {self.age} years old'

  def intro(self):
    return f'I am {self.name}'