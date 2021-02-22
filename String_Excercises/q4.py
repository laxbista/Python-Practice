# Exercise Question 4: Arrange string characters such that lowercase letters should come first
# Given an input string with the combination of the lower and upper case arrange characters in
# such a way that all lowercase letters should come first.
str = "PyNaTive"
lower = []
upper = []
for i in str:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
newString = ''.join(lower + upper)
print(newString)