#5) მომხმარებელს შეაყვანინე რიცხვები, მანამ სანამ არ შეიყვანს 0, ყოველი რიცხვის შემდეგ დაბეჭდე
#"დადებითია" ან "უარყოფითია".დაბეჭდე ბოლოს რიცხვების ჯამი.
#გამოიყენე while loop.
sum = 0
while True:
    nums = int(input("enter any nums or 0 : "))
    if nums > 0:
        print("დადებითია")
        sum = sum+nums

    else:
        print("უარყოფითია")
        sum = sum+nums
    if nums == 0:
        break

print(f"sum = {sum}")
