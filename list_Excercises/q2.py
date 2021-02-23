# Exercise Question 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# for i in list1:
#     for j in list2:
#         if list1.index(i) == list2.index(j):
#             print(i + j)
# Using List comphrension
newlist = [i + j for i, j in zip(list1, list2)]
print(newlist)