# 4) შექმენი ფუნქცია რომელიც მიიღებს სიტყვების სიას და დააბრუნებს მხოლოდ იმ სიტყვებს რომლებიც იწყება დიდი ასოთი

def words(list1):
    
    list2 = []

    for i in range(len(list1)):
        if list1[i][0] == list1[i][0].upper():
            list2.append(list1[i])

    return list2

print(words(["Giorgi", "andria", "luka", "Mamuka"]))