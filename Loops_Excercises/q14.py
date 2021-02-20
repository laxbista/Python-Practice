# Exercise Question 14: Reverse a given integer number 76542
num = 76542
reverse_num = 0
while num > 0:
    reminder = num % 10
    reverse_num = (reverse_num * 10) + reminder
    num = num // 10
print(reverse_num)

