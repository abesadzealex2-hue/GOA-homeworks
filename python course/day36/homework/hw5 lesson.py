# 5) შექმენი ფუქნცია რომელიც იღებს რიცხვების სიას და აბრუნებს მათ საშუალოს

def len1_sum1():
    sum1 = 0
    list1 = [1, 7, 89, 56, 62, 98]

    for i in range(len(list1)):
        sum1 += list1[i]

    print(sum1 / len(list1))

len1_sum1()