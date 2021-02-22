# Exercise Question 9: Given a string, return the sum and average
# of the digits that appear in the string, ignoring all other characters
import re

str1 = "English = 78 Science = 83 Math = 68 History = 65"
total = 0
List = [int(i) for i in str1.split() if i.isdigit()]  # Using List comprehension
for num in List:
    total += num

average = total / len(List)
print(total, average)
