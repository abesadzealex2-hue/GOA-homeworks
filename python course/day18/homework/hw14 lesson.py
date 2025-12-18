#14)შექმენი სია და შეინახე 3 ელემენტი --> მოიძიე ინფორმაცია და შეასრულე შემდეგი დავალება --> გამოიტანეთ სიის
# თითოეული ელემენტი ცალ ცალკე ---> "ინდექსები" - ს <---   გამოყენებით

#ინფორმაციას მოიძიებთ შემდეგი საიტიდან ---> w3school.com + რა გაინტერესებთ <---

 
#List items are indexed and you can access them by referring to the index number:
#ჩამოთვლილი საგნები არის ინდექსირებული და შეგიძლია მიუთითო ინდექსის რიცხვი

#ExampleGet your own Python Server
#აიღე შენი პითონის სერვერი
#Print the second item of the list:
#დაპრინტე მეორე საგანი სიაში

#thislist = ["apple", "banana", "cherry"]
# ეს სია [ "ბანანი" , "ალუბალი"]
#print(thislist[1])
#დაპრინტე სიიდან 1 საგანი

print(1)

this_list = [ "banana" , "cherry"]
print (this_list[1])


#Negative Indexing
#ნეგატიური ინდექსი
#Negative indexing means start from the end
#როცა 1 მიეთითება ბოლო საგანს , მეორე მეორეს და მესამე პირველს

#-1 refers to the last item, -2 refers to the second last item etc.
#ნომერი 2 მიეთითება ბოლოდან მეორე საგანს და ა.შ.

#Example
#Print the last item of the list:
#დაპრინტე ბოლო საგანი

#thislist = ["apple", "banana", "cherry"]
#print(thislist[-1])

print(2)

this_list = [ "banana" , "cherry"]
print (this_list[-2])

#Range of Indexes
#ინდექსის სიახლოვე
#You can specify a range of indexes by specifying where to start and where to end the range.
#შეგიძლია დააკონკრეტო ინდექსების მაშტაბი, იმის დაზუსტებით თუ სად დაიწყო და სად დაასრულო

#When specifying a range, the return value will be a new list with the specified items.
#როდესაც აკონკრეტებ მაშტაბს, დაბრუნების ღირებულება იქნება ახალი სია დაკონკრეტებული საგნებით.

#Example
#Return the third, fourth, and fifth item:

print(3)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#By leaving out the end value, the range will go on to the end of the list:

#Example
#This example returns the items from "cherry" to the end:

print(4)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:

#Example
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

print(5)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:

#Example
#Check if "apple" is present in the list:

print(6)

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

else:
  print("no")


print("0")

print (bool (""))

