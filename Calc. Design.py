

#SELF DESIGNED CALCULATOR
a=float(input('Enter the very first number of your choice', ))
b=input("Enter the desired mathematical operators", )
c=float(input('Enter the very second number of your choice', ))
if b=='+':
    print('The sum of the given two numbers is', a+c)
elif b=='-':
    print('The difference of the given two numbers is', a-c)
elif b=='*':
    print('The product of the given two numbers is', a*c)
elif b=='/':
    print('The division of the given two numbers is', a/c)
else:
    print('INVALID OPERATOR')
