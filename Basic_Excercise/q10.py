# Question 10: Given a two list of numbers create a new list
# such that new list should contain only odd numbers from the
# first list and even numbers from the second list
def oddAndEvenList(myList1, myList2):
    evenNum = []
    oddNum = []

    for num in myList1:
        if num % 2 != 0:
            evenNum.append(num)
    print("Odd Num frm list1: ", evenNum)
    for num in myList2:
        if num % 2 == 0:
            oddNum.append(num)
    print("Even num frm list2: ", oddNum)
    return evenNum + oddNum


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print("Result of odd and even list: ", oddAndEvenList(list1, list2))
