# Exercise Question 17: Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"

for i in str1.split():
    if i.isalpha() or i.isdigit():
        continue
    else:
        print(i)