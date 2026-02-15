# 3) შექმენით ფუნცქცია სახელად sum_numbers რომელიც პარამეტრად მიიღებს რიცხვების სიას [10, 20,30, 100, 200, 500 ] დაწერე ფუნქცია რომელიც
# დააბრუნებს მოცემული რიცხვების ჯამს

def sum_numbers(list1):
    sum1 = 0
    for i in range(len(list1)):
        sum1 += list1[i]
    return sum1
list1 = [ 10, 20,30, 100, 200, 500 ]
print(sum_numbers(list1))

