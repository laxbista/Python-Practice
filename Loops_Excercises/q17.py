# Exercise Question 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

number_of_terms = 5

start = 2
sum = 0
for i in range(0, number_of_terms):
    print(start, end=" ")
    sum += start
    start = (start * 10) + 2
print("\nSum:",sum)
