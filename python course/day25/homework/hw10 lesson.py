#10) შექმენი list: tasks = ["homework", "clean room", "exercise"] მომხმარებელს ჰკითხე Are you sure
#you want to delete all tasks? (yes/no). თუ "yes" მთლიანად 
#გაასუფთავე ლისთი, თუ "no" არაფერი შეცვალო.

tasks = ["homework", "clean room", "exercise"]
answer = input("Are you sureyou want to delete all tasks? type yes or no : ")

if answer == "yes":
    tasks.clear()
    print(tasks)

elif answer == "no":
    print("nothing")

else:
    print("i dont know what do u want")