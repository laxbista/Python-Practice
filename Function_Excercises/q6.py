# Exercise Question 6: Write a recursive function to calculate the sum of numbers from 0 to 10

def recursiveFunc(num):
    if num > 0:
        return num + recursiveFunc(num - 1)
    else:
        return 0


print(recursiveFunc(10))
