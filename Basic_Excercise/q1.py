# Question 1: Given a two integer numbers return their product
# and  if the product is greater than 1000, then return their sum

def product_sum(num1, num2):
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product


print(product_sum(20, 30))
print(product_sum(40, 30))
