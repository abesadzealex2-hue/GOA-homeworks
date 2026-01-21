sentence = "მე მქვია ალექსი"

word = ""

i = 0

while i < len(sentence):
    if sentence[i] != " ":
        word += sentence[i]
    
    else:
        
        print(word)
        word = ""
    i += 1

print(word)


