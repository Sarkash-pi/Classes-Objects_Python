from animal import Animal

# instance / object!

dog = Animal(kind='dog', name='Luna', age=3)
cat = Animal(kind='cat', name='Suzgi', age=5)
ham = Animal(kind='Hamster', name='JoJo',  age=2)



print(dog.speak())
print(dog.intro())

print(cat.speak())
print(cat.intro())

print(ham.speak())
print(ham.intro())