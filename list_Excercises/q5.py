# Exercise Question 5: Given a two Python list. Iterate both lists simultaneously
# such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# reverselist2 = list2[::-1]
# for i in list1:
#     print(i)
# for j in reverselist2:
#     print(j)
for i,j in zip(list1, list2[::-1]):
    print(i,j)