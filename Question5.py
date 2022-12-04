# Question 5
# Write a Python function to calculate the factorial of a number. The function accepts the number as an argument.

def factorial():
    num = int(input("Entr the number you want to find the factorial of: "))
    if num<0:
        print("Invalid Entry! The number must be a positive integer")
    else:
        fact = 1
        for i in range(1,num+1):
            fact = fact * i
        print("The factoral of",num,"is",fact)

factorial()