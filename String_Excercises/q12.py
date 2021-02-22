# Exercise Question 12: Find the last position of a substring “Emma” in a given string
# Where in the string is the last occurrence of the substring “Emma”?:


str1 = "Emma is a data scientist who knows Python. Emma works at google."
search= "Emma"

occur = str1.rfind(search)
print(occur)
