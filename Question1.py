#question 1:
#Write a Python function to find the Max of three numbers

def greatestNumber(a,b,c):
    if a>b and a>c:
        print("a",a," is the greatest")
    elif b>a and b>c:
        print("b",b," is the greatest")
    else:
        print("c",c," is the greatest")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
greatestNumber(a,b,c)