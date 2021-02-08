# Question 11: Write a code to extract each digit from an integer
# , in the reverse order

def reverseOrder(num):
    while num > 0:
        reverseNum = num % 10
        num = num // 10
        print(reverseNum, end = ' ')


reverseOrder(12345)
