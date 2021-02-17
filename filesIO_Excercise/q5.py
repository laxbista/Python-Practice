# Exercise Question 5: Accept list of 5 float numbers as a input from user
floatNumbers = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)

print("User List is ", floatNumbers)