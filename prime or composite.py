# 1. Program to Check if a Number is Prime or Composite

a=float(input('Enter the number to get its multiple', ))
for i in range(1,26):
    i=a*i
    print(i)

a= 5 #int(input('enter any number', ))
c=a//2
for i in range(2,c+1):
    rem=a%i
    if rem==0:
     print('Composite Number.')
    else:
        print('prime number')
           




# Function to check if a number is prime or composite
def check_prime_composite(num):
    if num <= 1:
        return "Neither prime nor composite"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Composite"
    return "Prime"

# Input from user
number = int(input("Enter a number: "))
result = check_prime_composite(number)
print(f"The number {number} is {result}.")


# Input from user
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}.")


