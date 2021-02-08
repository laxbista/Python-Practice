# Question 2: Given a range of first 10 numbers,
# Iterate from start number to the end number and
# print the sum of the current number and previous number

def sumPro(num):
    preNum = 0
    for i in range(num):
        total = preNum + i
        print("Current Number: ", i, "Previous Number: ", preNum, "Sum: ", total)
        preNum = i


sumPro(10)
