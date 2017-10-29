def LargePF(a):
    pf=2
    while(a>pf):
        if a%pf==0:
            a=a/pf
            pf=2
        else :
            pf+=1
    return pf
x=int(input('Enter the number for which you want to find the largest prime factor:\t'))
if x<2 and x>0:
    y=1
else:
    y=LargePF(x)
print('The largest Prime factor of',x,'is',y)
