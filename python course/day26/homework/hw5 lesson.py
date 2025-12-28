#5) მომხმარებელს შემოაყვანინე რიცხვები, ეს რიცხვები დაამატე სიაში და გამოითვალე ამ რიცხვების 
#საშუალო არითმეტიკული.
nums = []
sum_number=0
len_number=0

while True:
    number=input("enter any number:")
    if number == "გამოთვალე საშუალო":
        break
    len_number=len_number + 1
    sum_number=sum_number+int(number)
    nums.append(int(number))

print (sum_number/len_number)
print(nums)