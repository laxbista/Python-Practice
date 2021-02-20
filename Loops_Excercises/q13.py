# Exercise Question 13: Write a loop to find the factorial of any number

def factorialOf(Num):
    fact = 1
    for i in range(1, Num + 1):
        fact = fact * i
    print(fact)


factorialOf(5)
