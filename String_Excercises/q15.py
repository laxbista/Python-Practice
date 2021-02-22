# Exercise Question 15: Remove special symbols/Punctuation from a given string
import string
str1 = "/*Jon is @developer & musician"

newString = str1.translate(str.maketrans("","",string.punctuation))
print(newString)