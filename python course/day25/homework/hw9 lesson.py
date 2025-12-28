#9) შექმენი list: nums = [1, 2, 3, 4] მომხმარებელს შეაყვანინე: ინდექსი და რიცხვი, თუ ინდექსი
#list-ის საზღვრებშია გამოიყენე insert() ჩასამატებლად, თუ ინდექსი 
#ლისტზე დიდია მაშინ გამოიყენე append()

nums = [1, 2, 3, 4]

index = int(input("enter any index : "))
number = int(input("enter any number : "))

if index <= 3:
    nums.insert(index, number)
else:
    nums.append(number)

print(nums)