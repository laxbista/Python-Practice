# Exercise Question 10: Given an input string, count occurrences of all characters within a string
str = "Apple"
Dict = {}
for i in str:
    count = str.count(i)
    Dict[i] = count
print(Dict)
