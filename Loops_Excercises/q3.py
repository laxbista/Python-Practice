# Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number
# For example user given 10 so the output should be 55

userInput = int(input("Enter Number:"))
Total = 0
for i in range(1, userInput + 1):
    Total = Total + i
    print(i, Total)
print("Total", Total)
