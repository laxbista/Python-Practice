# Exercise Question 5: Given a list iterate it and display
# numbers which are divisible by 5 and
# if you find number greater than 150 stop the loop iteration

myList = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in myList:
    if i %5 ==0 and i<=150:
        print(i)

