# Question 3
# Write a Python function to multiply all the numbers in a list

def productOfElements(lists):
    product = 1
    for i in lists:
        product = product * i
    return product

a = int(input("Enter how many elements you want to input: "))
l = []
for j in range(0,a):
    b = int(input("enter the elements: "))
    l.append(b)
print(l)
print(productOfElements(l))