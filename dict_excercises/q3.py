# Exercise 3: Access the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
            }
        }
    }
}
getValue = sampleDict['class']['student']['marks']['history']
print(getValue)
