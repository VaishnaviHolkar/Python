#Write a program to swap two numbers (with and without using a third variable).
print("Swapping without using third variable")
a=int(input("Enter the first value:- "))
b=int(input("Enter the second value:- "))
a=a+b
b=a-b
a=a-b
print(a)
print(b)