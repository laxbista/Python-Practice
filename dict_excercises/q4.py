# Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

DefaultValues = dict.fromkeys(employees, defaults)
print(DefaultValues)

print(DefaultValues['Kelly'])