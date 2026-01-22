# 4) შექმენით სტრინგის ცვლადი და ცარიელი სია. სტრინგში მყოფი დიდი ასოები გახადეთ პატარა და
# ამ სიაში ჩაამატეთ, ხოლო სტრინგში მყოფი პატარა ასოები გახადეთ დიდი და ასევე ჩააგდეთ ამ სიაში.
# დაპრინტეთ საბოლოო სია,
# გამოიყენეთ while ციკლი.

str1 = "HiDRoeLeqtRosadguri"

list1 = []

i = 0

while i < len(str1):
    if str1[i] == str1[i].lower() :
        list1.append(str1[i].upper())
        

    elif str1[i] == str1[i].upper():
        list1.append(str1[i].lower())

    i += 1
        
print(list1)