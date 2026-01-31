def newlist():
    names = ["alex" , "Gio" , "nana" , "Zurabi" , "andria"]
    empty = []

    i = 0
    while i < len(names):
        if names[i] == names[i].capitalize():
            names.pop(i)
        else:
            empty.append(names[i] * 3)
            i += 1
    print(names)
    print(empty)

newlist()