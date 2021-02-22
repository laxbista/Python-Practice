# Exercise Question 5: Count all lower case, upper case, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
digits = 0
char = 0
sym = 0

for i in str1:
    if i.isalpha():
        char += 1
    elif i.isnumeric():
        digits += 1
    else:
        sym += 1
print(digits, char, sym)
