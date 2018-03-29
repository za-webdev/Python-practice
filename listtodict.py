
#A function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict():
  new_dict = zip(name,favorite_animal)
  a= dict(new_dict)
  print a
  	
  
make_dict()