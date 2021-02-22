# Exercise Question 2: Given 2 strings, s1 and s2,
# create a new string by appending s2 in the middle of s1
def newString(s1, s2):
    MiddleS1 = len(s1) // 2
    new_String = s1[:MiddleS1] + s2 + s1[MiddleS1:]
    print(new_String)


newString("Ault", "Kelly")
