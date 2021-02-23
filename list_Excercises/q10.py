# Exercise Question 10: Given a Python list, remove all
# occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
newlist =[]
for i in list1:
    if i!=20:
        newlist.append(i)
print(newlist)
