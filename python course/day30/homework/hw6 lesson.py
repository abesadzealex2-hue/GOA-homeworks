# 6) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 
# 5-ზე მეტი სიგრძეში ან დგანან კენტ
# ინდექსზე. გამოიყენეთ remove() ფუნქცია.

list1 = ["GOA" , "FRUIT" , "HOME" , "ITEM" , "KARAVI" , "DIVANI" , "FANDURI" , "GITARA"]

i = 0

while i < len(list1):
    if len(list1[i]) > 5 or i % 2 == 1:
        list1.remove(list1[i])

    else:
        i += 1
    
print(list1)

