# Exercise Question 16: Removal all the characters other than integers from string

str = "I am 25 years and 10 months old"

for i in str:
    if i.isdigit():
        print(i,end="")
