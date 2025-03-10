
num=int(input("enter the number",))
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0 or num == 1:
    print(1)
else:
    fact = 1
for i in range(2, num + 1):
    fact *= i
    print(fact)









#  3. Program to Find the Sum of Digits of a Given Number


# Function to calculate the sum of digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Input from user
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}.")


