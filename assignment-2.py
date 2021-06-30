import random
no_of_persons=int(input("enter participant :"))
l=[]
for i in range(no_of_persons):
    l.append(str(input()))
# l=['rani','raju','sean','clare','harry','walker','taylor','siva','rax','priya']
pr=random.randint(0,no_of_persons-1)
print("lottery winner is :",l[pr])
