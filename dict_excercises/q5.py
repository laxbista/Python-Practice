# Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
# Extract key name and salary
keys = ["name", "salary"]
newDict = {}
for k in keys:
    value = sampleDict[k]
    newDict[k] = value
print(newDict)
