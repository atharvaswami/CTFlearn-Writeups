ans=0
with open('data.dat') as F:
    L = F.readlines()  
    for S in L:
        try:
            if(S.count('0')%3==0 or S.count('1')%2==0):
                ans+=1
        except EOFError:
            break
print("CTFlearn{" + str(ans) + "}")
F.close()