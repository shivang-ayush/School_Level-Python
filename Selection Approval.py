
A= '''Dear NAME
Your are selected for our production Team.
Date:- DATE
'''
NAME= input("Enter your name",)
DATE= input("Enter today's date",)
A= A.replace("NAME", NAME)
A= A.replace("DATE", DATE)
print(A)

