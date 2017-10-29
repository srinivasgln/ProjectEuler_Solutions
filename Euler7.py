def primeLocator(lr,ur,pr):
    count=0
    for m in range(lr,ur+1):
        check=True
        for n in range(lr,int(m**0.5)+1):
            if m%n==0:
                check=False
                break
        if check:
            count+=1
            if count==pr:
                primeNum=m
                return primeNum

inp1=int(input('Enter your lower natural number for finding prime numbers:'))
inp2=int(input('Enter your upper natural number for finding prime numbers:'))
inp3=int(input('Which prime number you would like to find?'))
if inp2==2:
    print('invalid input')
elif (inp1>1):
    a=primeLocator(inp1,inp2,inp3)
    print('The',inp3,'th prime number  between',inp1,inp2,'is',a)
