# Exercise 1: Below are the two lists convert it into the dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict = {}

for k in keys:
    for v in values:
        dict[k] = v
print(dict)
