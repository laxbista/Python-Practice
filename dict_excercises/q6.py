# Exercise 6: Delete set of keys from a dictionary
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]

for k in keysToRemove:
    del sampleDict[k]
print(sampleDict)
