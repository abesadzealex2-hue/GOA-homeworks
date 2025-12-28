#1) შექმენი list: names = ["nika", "luka", "giorgi"] მომხმარებელს შეაყვანინე: ინდექსი და სახელი,
#insert()-ის გამოყენებით ჩასვი სახელი
#მითითებულ ადგილას და დაბეჭდე შედეგი

names = ["nika", "luka", "giorgi"]
index = int(input("type index: "))
name = input("type name: ")
names.insert(index , name)
print(names)
