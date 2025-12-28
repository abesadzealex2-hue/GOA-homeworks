#4) შექმენი list: colors = ["red", "blue", "green", "yellow"] მომხმარებელს შეაყვანინე ფერი, თუ
#არსებობს  დაბეჭდე მისი index(), თუ არა  
#დაბეჭდე "Not found"

colors = ["red", "blue", "green", "yellow"]
color2 = input(" enter the second color: ")
if color2 in colors:
    print(colors.index(color2))
else:
    print("not founded")