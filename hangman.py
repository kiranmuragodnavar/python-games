import random
lis = ["Srujan"]


n = random.choice(lis)
l2 = []

for i in range(len(n)):
    l2.append(0)

print("Let's start the Game:")

m = 0
k = 0
check=2
for i in range(len(n)):
    s = 0
    inp = 0
    if(k==2):
        #print("You lost it sorry")
        check=0
        break
    
    while(n[i] != inp):
        inp = input("Enter the input:")
        if(n[i] == inp):
            print("Clever buddy :))")
            l2[i] = inp
            print("You took", s, " guesses")
            print(l2)
            m = m+s
        else:
            print("No Buddy :(")
            s += 1
            k += 1
            print(l2)
            if(k==2):
               # print("You lost it sorry")
                check=0
                break
print("The answer was",*l2,end='')
print("You took totally",k,"guesses")
if(check):
    print("You won it")
else:
    print("You lost it")

   
