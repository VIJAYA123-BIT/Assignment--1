import random
no_of_persons=int(input())

cost_of_ticket=int(input())
total=no_of_persons*cost_of_ticket
l=[]
for i in range(no_of_persons):
    l.append(input())
# l=['rani','raju','sean','clare','harry','walker','taylor','siva','rax','priya']
pr=random.choice(l)
print("the lottery winner is %s and the lottery that the participant won was:%d"%(pr,total))
