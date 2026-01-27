# 1) შექმენით სახელებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის d, მაშინ ახალ სიაში
# ჩაამატეთ სახელი "NIKA", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო K-თი, მაშინ სიაში ჩაამატეთ სახელი "GOGA"
# , სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

names1 = ["dima" , "goga" , "alex" , "nika" , "kaki" , "andria" , "nini"]

new_list = []

for i in names1:
    if i == i.lower() and i[0] == "d":
        new_list.append("NIKA")

    elif i == i.upper() or i[0] == "k":
        new_list.append("GOGA")

    else:
        new_list.append("ლიდერი")

print(new_list)