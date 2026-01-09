#1) მომხმარებელს შემოაყვანინე წინადადება. დაბეჭდე თითოეული სიტყვა ცალ–ცალკე
#for loop-ის გამოყენებით. თითოეული სიტყვა დაბეჭდე capitalize()-ით.

sentence = input("enter sentences : ")

words = sentence.split()
print(words)


for i in range (len(words)):
    print(words[i].capitalize())