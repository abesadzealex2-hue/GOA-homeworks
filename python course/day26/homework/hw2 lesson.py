#2) შექმენი ცარიელი სია. მომხმარებელს შეაყვანინე რიცხვები სანამ "stop"-ს არ დაბეჭდავს, ყოველი
#ახალი რიცხვი: თუ ნაკლებია 50-ზე → ჩასვი სიის დასაწყისში (insert), თუ მეტია ან ტოლია 50-ის 
#→ დაამატე ბოლოში 
#(append), ბოლოს დაბეჭდე სია

numbers = []

while True:
    nums = input("enter any number : ")
    if nums == "stop":
        break
    if int(nums) < 50:
        numbers.insert(0,int(nums))
    elif int(nums) >= 50:
        numbers.append(int(nums))

print(numbers)