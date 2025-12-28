#შექმენი ცარიელი სია, for ციკლით 1 დაან 10-მდე დაამატე სიაში რიცხვები, remove-ის გამოყენებით
#წაშალე ყველა კენტი რიცხვი  და ბოლოს დაბეჭდე საბოლოო 
#სია]~

nums = []

for i in range(1,11):
    list.append(i)

    for numbers in nums:
        if numbers % 2 == 1:
            numbers.remove(nums)

        print(nums)