# 5)შექმენი სია სადაც შეიყვანთ როგორდც დადებით ასევე უარყოფით რიცხვებს,შენი დავალებაა გაიგო
# სიაშ მყოფი დადებით რიცხვების ჯამი და უარყოფით რიცხვების რაოდენობა

nums = [-5 , 6 , 88 , -999 , 124 , 777 , -3 , 500 , -432]

more_than_0 = 0

less_than_0 = 0

for i in range(len(nums)):
    if nums[i] > 0:
        more_than_0 += nums[i]

    elif nums[i] < 0 :
        less_than_0 += 1

print(nums)

print(more_than_0)

print(less_than_0)

