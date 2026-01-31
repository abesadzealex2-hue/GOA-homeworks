# 2) შექმენით ფუნქცია. შექმენით რიცხვებით სავსე სია, დაბეჭდეთ სიის უდიდესი
# ელემენტი. არ გამოიყენოთ max() ფუნქცია,
# გამოიყენეთ for ციკლი. გამოიძახეთ ფუნქცია.

def function2():
    nums = [1, 34, 12, 5, 2, 9, 89]
    biggest = nums[0]

    for i in nums:
        if i > biggest:
            biggest = i

    print(biggest)

function2()