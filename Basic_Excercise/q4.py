# Question 4: Given a string and an integer number n,
# remove characters from a string starting from zero
# up to n and return a new string
# for example, removeChars("pynative", 4)
# so output must be tive. Note: n must be less than the length of the string.
def removeStr(string, n):
    if n < len(string):
        return string[n:]
    else:
        return "N must be less than the length of the string"


print(removeStr("pynative", 4))
print(removeStr("pynative", 8))
