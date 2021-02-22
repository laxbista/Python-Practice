# Exercise Question 7: String characters balance Test
# We’ll say that a String s1 and s2 is balanced
# if all the chars in the s1 are there in s2. characters position doesn’t matter.

def strBalTest(s1, s2):
    bool =True
    for i in s1:
        if i in s2:
            continue
        else:
            return False
    return bool


print(strBalTest("Yn", "PYnative"))
print(strBalTest("Ynf", "PYnative"))
