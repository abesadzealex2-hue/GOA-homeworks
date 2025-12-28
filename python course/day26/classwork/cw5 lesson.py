#შექმენით სია ["cat", "elephant", "dog", "tiger", "ox"], წაშალეთ ყველა სიტყვა 
#რომლის სიგრძეც ნაკლებია
#4-ზე

animals = ["cat", "elephant", "dog", "tiger", "ox"]
i = 0

while i < len(animals):
    if len(animals[i]) < 4:
        animals.pop(i)

    else:
        i=i+1

print(animals)
