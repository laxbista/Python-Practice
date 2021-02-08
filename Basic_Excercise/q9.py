# Question 9: Reverse a given number and return true
# if it is the same as the original number
# Ex-original number 121. The original and reverse number is the same

def reverseCheck(number):
    originalNum = number
    reverseNum = 0
    while number > 0:
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if originalNum == reverseNum:
        return True
    else:
        return False


print("The original and reverse number is the same:", reverseCheck(121))
