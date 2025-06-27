import random as rnd
l, l1, l2, l3 = [], [], [], []
sum1, sum2, sum3 = 0, 0, 0

for i in range (0,15):
    l.append(rnd.randint(1,100))
print(l)
for i in range(5):
    l1.append(rnd.choice(l))
    
    l2.append(rnd.choice(l))
    l3.append(rnd.choice(l))
for i in range(5):
    sum1+=l1[i]
    sum2+=l2[i]
    sum3+=l3[i]
if sum1>sum2 and sum1>sum3 :
    print(f"{l1} is the winner with the sum {sum1} other sum were {sum2,sum3}")
elif sum2>sum1 and sum2>sum3: 
    print(f"{l2} is the winner with the sum {sum2}")
else:

    print(f"{l3} is the winner with the sum {sum3}")

    
