# Exercise Question 3: Given 2 strings, s1, and s2 return a new string made of the first,
# middle and last char each input string
def newString(s1, s2):
    Mids1 = len(s1)//2
    Mids2 = len(s2)//2
    new_String = s1[:1] + s2[:1] + s1[Mids1] +s2[Mids2] + s1[-1] +s2[-1]
    print(new_String)


newString("America", "Japan")
