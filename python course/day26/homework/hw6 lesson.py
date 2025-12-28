#6) მომხმარებელს შემოაყვანინე რიცხვები, შექმენი ორი სია დადებითი და 
#უარყოფითი სიებისთვის, დადებითი რიცხვები დაამატე დადებითი რიცხვებისთვის განკუთვნილ სიაში,
#უარყოფითი რიცხვები კი პირიქით
positive = []
negative = []
while True:
    nums = input("enter any nums : ")
    if nums == "stop":
        break
    if int(nums) > 0:
        positive.append(int(nums))

    elif int(nums) < 0:
        negative.append(int(nums))

print("negative list" , negative)
print("positive list" , positive)