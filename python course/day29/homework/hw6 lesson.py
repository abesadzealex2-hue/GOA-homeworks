# 6)მომხმარებელს შემოატანინე რაიმე სტრინგი,შენი დავალებაა დაითვალო თუ რამდენი ცალი
# ხმოვანი და რამდენი ცალი თანხმოვანი გვხვდება მის მიერ შემოყვანილ სტრინგში



sentence = input("enter any letter (georgian):")

vowels = "aeiou"

consonant = 0


i = 0
while i < len(sentence):
    if sentence[i] in vowels:
        vowels += 1

    else:
        consonant += 1

print(vowels)
print(consonant)

    

    



