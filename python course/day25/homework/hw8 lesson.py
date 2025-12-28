#8) შექმენი list: animals = ["dog", "cat", "horse", "cow"] მომხმარებელს შეაყვანინე 
#ცხოველის სახელი, თუ არსებობს  დაბეჭდე მისი index-იმ, თუ არა  "Animal not found"

animals = ["dog", "cat", "horse", "cow"]

animal_name = input("enter any animal : ")

if animal_name in animals:
    print(animals.index(animal_name))

else:
    print("animal not found")