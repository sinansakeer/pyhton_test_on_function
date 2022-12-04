# Question 6
# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def uniqueElements(lists):
    uniqueList = []
    for i in lists:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

a = int(input("Enter how many elements you want in the list: "))
L = []
for i in range(0,a):
    b = int(input("Enter element: "))
    L.append(b)
print(L)
print(uniqueElements(L))