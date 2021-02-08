# Given a list of numbers, Iterate it and
# print only those numbers which are divisible of 5

def divByFive(listNum):
    for i in listNum:
        if i % 5 == 0:
            print(i)


myList = [10, 20, 33, 46, 55]
divByFive(myList)
