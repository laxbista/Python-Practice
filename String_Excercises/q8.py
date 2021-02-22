# Exercise Question 8: Find all occurrences of “USA” in given string ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
targetString = "USA"
lowerAllString = str1.lower()
count = lowerAllString.count(targetString.lower())
print("The USA count is:", count)
