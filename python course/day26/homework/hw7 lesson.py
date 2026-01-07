#7) მომხმარებელს შემოაყვანინე რიცხვები, ეს რიცხვები დაამატე სიაში, თუ ორი 
#მეზობელი ელემენტის ჯამი <50-ზე მაშინ წაშალე 
#მეორე ელემენტი, დაბეჭდე საბოლოო სია.
numbers = []
len = 0
while True:
    nums = input("enter any nums : ")
    if nums == "stop":
        break
    numbers.append(int(nums))
    len=len+1
    if len >= 2:
        if numbers[-1] + numbers[-2] < 50:
            numbers.pop()
            len=len-1
print(numbers)
print(f"len is { len } in numbers list")
        
