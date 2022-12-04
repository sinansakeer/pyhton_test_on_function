# Question 7
# Write a Python program to print the even numbers from a given list.

def evenElements(lists):
    evenList = []
    for i in lists:
        if i%2 == 0:
            evenList.append(i)
    return evenList

a = int(input("Enter how many elements you want in the list: "))
L = []
for i in range(0,a):
    b = int(input("Enter element: "))
    L.append(b)
print(L)
print(evenElements(L))