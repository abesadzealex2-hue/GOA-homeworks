#6) მომხმარებელს შემოაყვანინე რიცხვები, შექმენი ორი სია დადებითი და 
#უარყოფითი სიებისთვის, დადებითი რიცხვები დაამატე დადებითი რიცხვებისთვის განკუთვნილ სიაში,
#უარყოფითი რიცხვები კი პირიქით
positive = []
negative = []
while True:
    nums = input("enter any nums or stop: ")
    if nums == "stop":
        break
    if int(nums) > 0:
        positive.append(int(nums))

    elif int(nums) < 0:
        negative.append(int(nums))

print(f"negative numbers: {negative}" )
print(f"positive numbers: {positive}")