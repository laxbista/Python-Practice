# Question 5: Given a list of numbers, return True
# if first and last number of a list is same
def firstNum_lastNumList(listN):
    if listN[0] == listN[-1]:
        return True
    else:
        return False


numInList = [10, 20, 30, 40, 50]
numInList = [10, 20, 30, 40, 50]
print(firstNum_lastNumList(numInList))
