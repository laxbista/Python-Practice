# Exercise Question 8: Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]

myList = [10, 20, 30, 40, 50]
for i in range((len(myList)-1), -1, -1):
    print(myList[i])
