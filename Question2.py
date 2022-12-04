#Question 2
#Write a Python function to sum all the numbers in a list

def sumOfElements(lists):
    sum = 0
    for i in lists:
        sum = sum + i
    return sum

a = int(input("Enter how many elements you want to input: "))
l = []
for j in range(0,a):
    b = int(input("enter the elements: "))
    l.append(b)
print(l)
print(sumOfElements(l))