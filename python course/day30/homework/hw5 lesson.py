# 5) შექმენით სტრინგის ცვლადი და ცარიელი სია, თუ სტრინგის ასო არის პატარა, მაშინ ცარიელ სიაში ჩაამატეთ
# "%" ნიშანი, ხოლო თუ სტრინგის ასო არის დიდი, მაშინ ცარიელ სიაში ჩაამატეთ "@" ნიშანი. თუ მინუსების
# რაოდენობა სიაში არის ლუწი, მაშინ წაშალე ყველა "%" ნიშანი, ხოლო თუ მინუსების რაოდენობა სიაში არის კენტი,
# წაშალე ყველა "@" ნიშანი. "%" და "@" -ების თავიდან სიაში ჩასაგდებად გამოიყენეთ for ციკლი, ხოლო "%" ან "@"
#  -ების წასაშლელად გამოიყენეთ 
# while ციკლი.

word1 = "HIDRoelEqtrOSadguRiGFhffGF"

symbols = []

for i in range(len(word1)):
    if word1[i] == word1[i].lower():
        symbols.append("%")
    elif word1[i] == word1[i].upper():
        symbols.append("@")

i = 0

if len(symbols) % 2 == 0:
    while i < len(symbols):
        if symbols[i] == "%":
            symbols.pop(i)
        
        else:
            i += 1
else:
    while i < len(symbols):
        if symbols[i] == "@":
            symbols.pop(i)
        
        else:
            i += 1


print(symbols)






