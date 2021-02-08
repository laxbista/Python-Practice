# Question 12: Calculate income tax for the given
# income by adhering to the below rules
# Taxable income          rate(%)
# First $10,000              0
# Next $10,000               10
# The remaining               20
income = 45000
firstTaxableIncome = 10000
nextTaxableIncome = 10000
remainTaxIncome = income - (firstTaxableIncome + nextTaxableIncome)
incomeTaxPayable = (firstTaxableIncome * 0) + (nextTaxableIncome * 0.1) + (remainTaxIncome * 0.2)

print(incomeTaxPayable)
