# 3)შექმენი სია სადაც მოათავსებთ ინტეჯერ ტიპის მოანცემებს,შენი დავალებაა დაითვალო
# თუ რამდენი ცალი რიცხვი გვხვდება
# სიაში რომელიც არის 50 ზე მეტი

numbers = [11 , 13 , 66 , 98 , 86 , 568 , 75 , 545 , 32 , 3]

more_than_50_numbers = []

for i in range(len(numbers)):
    if numbers[i] > 50 :
        more_than_50_numbers.append(numbers[i])

print(more_than_50_numbers)