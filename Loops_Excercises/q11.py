# Exercise Question 11: Python program to display all the prime numbers within a range

def primeNum(firstNum, lastNum):
    for i in range(firstNum, lastNum + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)


primeNum(25, 50)