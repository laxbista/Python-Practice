# Exercise Question 1: Given a string of odd length greater 7,
# return a string made of the middle three chars of a given String
def middleThreeChars(str):
    if len(str) >= 7:
        mid_Chars = len(str) // 2
        print(str[mid_Chars - 1:mid_Chars + 2])
    else:
        print("Must have more than 7 characters")


str1 = "JhonDipPeta"
str2 = "JaSonAy"
middleThreeChars(str1)
middleThreeChars(str2)