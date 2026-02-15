# 14) დაწერეთ ფუნქცია, რომელიც მიიღებს ორ პარამეტრს და დააჯამებს ყველა რიცხვს გარკვეულ შუალედში.
# მაგალითად შეკრიბავს რიცხვებს 5-დან 100-მდე.

def calculator(first , second):
    result = 0
    for i in range(first , second):
        result += 1
    return result
print(calculator(4,34561))