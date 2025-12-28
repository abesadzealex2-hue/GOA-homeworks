#4) შექმენი ცარიელი სია. მომხმარებელს შემოაყვანინე რიცხვები,
# თუ რიცხვი უკვე არსებობს სიაში შეწყვიტე შეყვანა, სხვა შემთხვევაში დაამატე რიცხვები 
#სიაში, ბოლოს დაბეჭდე მთლიანი სია

nums = []

while True:
    num = int(input("enter any number : "))
    if num in nums:
        break
    else:
        nums.append(num)
print(nums)