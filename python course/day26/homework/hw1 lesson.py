#1) შექმენი ცარიელი სია.მომხმარებელმა შეიყვანოს რიცხვები მანამ, სანამ
#  არ დაწერს "stop".დაამატე მხოლოდ დადებითი რიცხვები სიაში, უარყოფითი რიცხვები არ დაამატო, ბოლოს დაბეჭდე სია

numbers = []   

while True:
    nums = input(" type any nums or stop: ")
    if nums == "stop":
        break
    if int(nums) > 0:
        numbers.append (int(nums))
print(numbers)