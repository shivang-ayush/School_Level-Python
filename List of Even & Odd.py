a=int(input('Enter a desired number of your own choice', ))
b=int(input('Enter a desired number of your own choice', ))
if a>=b:
    print('INVALID')
else:
    for i in range(a,b+1):
        if i%2==0:
            print("Even Number:, ", i)
        else:
            print("Odd Number::, ", i)
