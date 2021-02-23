# Exercise Question 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
empty = ""
newlist = []
for i in list1:
    if i != empty:
        newlist.append(i)
print(newlist)

