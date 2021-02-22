# Exercise Question 6: Given two strings, s1 and s2, create a mixed String
# Note: create a third-string made of the first char of s1 then the last char of s2,
# Next, the second char of s1 and second last char of s2,
# and so on. Any leftover chars go at the end of the result.
s1 = "Abc"
s2 = "Xyz"
s2 = s2[::-1]
# print(s2)
length_s1 = len(s1)
length_s2 = len(s2)

newString = ""
for i in range(length_s1):
    if i < length_s1:
        newString = newString + s1[i]
    if i < length_s2:
        newString = newString + s2[i]

print(newString)
