# 4) შექმენით ფუნქცია. მომხმარებელს შემოატანინეთ წინადადების სტრინგი. დათვალე,
# რამდენი სიტყვის სიგრძე არის 4-ზე მეტი. დაპრინტე ასეთი სიტყვების რაოდენობა. დაწერეთ
# ეს დავალება ორნაირად - split() ფუნქციით და split()
# ფუნქციის გარეშე.

print("With split")

def function():
    more_than4 = 0
    text = input("enter any str: ")
    words = text.split()

    for i in range(len(words)):
        if len(words[i]) > 4:
            more_than4 += 1

    print(more_than4)
function()

print("Without split")

def function2():
    sentence = input("enter any sentence : : ")
    count1 = 0
    len1 = 0

    for i in range(len(sentence)):
        if sentence[i] != " ":
           len1 += 1
        else:
            if len1 > 4:
                count1 += 1
            word_len = 0

    if len1 > 4:
        count1 += 1

    print(count1)

function2()




