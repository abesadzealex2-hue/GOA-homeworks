#6) შექმენი ცარიელი list, მომხმარებელს 5-ჯერ შეაყვანინე რიცხვი, ყველა დაამატე list-ში
#და საბოლოოდ for loop-ის გამოყენებით დააჯამე რიცხვები რომელიც გექნება ლისტში

nums = []
amount = 0
num1 = int(input("enter any number: "))
num2 = int(input("enter any number: "))
num3 = int(input("enter any number: "))
num4 = int(input("enter any number: "))
num5 = int(input("enter any number: "))

nums.append(num1)
nums.append(num2)
nums.append(num3)
nums.append(num4)
nums.append(num5)

for i in range(0 , 5):
    amount += nums[i]
print(amount)