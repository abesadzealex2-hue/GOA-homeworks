# 4)შექმენი სია და შეიყვანე სტრიგნები პატარა ასოებით,შენი დავალებაა შეამოწმო,თუ სტრინგი
#შეიცავს 5 ასოზე
# მეტს მაშინ ასეთი სიტყვები ჩაამატე ახალ სიაში ოღონდ პირველი ასო ქონდეთ დიდი ,ხოლო თუ სიტყვა
# შეიცავს 5 ასოზე ნაკლებს მაშინ დაამატე ეს ელემენტებიც სიაში ოღონდ ყველა ასო ქონდეთ დიდი

strings1 = ["goa" , "python" , "academy" , "money" , "chad"]

big_strings = []

small_strings = []


for i in range(len(strings1)):
    if len(strings1[i]) >= 5 :
        big_strings.append(strings1[i].capitalize())

    elif len(strings1[i]) < 5 :
        small_strings.append(strings1[i].upper())


print(strings1)

print(big_strings)

print(small_strings)