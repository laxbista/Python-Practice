# Exercise Question 13: Split a given string on hyphens into several substrings and display each substring
#
str1 = "Emma-is-a-data-scientist"

# hyphen = "-"
# for i in str1:
#     if i != hyphen:
#         print(i, end="")
#     elif i == hyphen:
#         print("")
#         continue
#Using split method below
subs = str1.split("-")
for i in subs:
    print(i)