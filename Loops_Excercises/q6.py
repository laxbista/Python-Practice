# Exercise Question 6: Given a number count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.

def totalDigits_InNum(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    print(count)


totalDigits_InNum(12345)
