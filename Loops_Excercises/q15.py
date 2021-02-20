# Exercise Question 15: Use a loop to display elements from a given list which are present at even positions
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in myList:
#     index = myList.index(i)
#     if index % 2 == 1:
#         print(myList[index])

for i in myList[1::2]:
    print(i, end=" ")