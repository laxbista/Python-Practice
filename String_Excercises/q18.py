# Exercise Question 18: From given string replace each punctuation with #
from string import punctuation
str1 = '/*Jon is @developer & musician!!'

hashtag = "#"
for i in punctuation:
    str1 = str1.replace(i,hashtag)
print(str1)