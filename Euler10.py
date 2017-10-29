def primeSum(lr,ur):
    primeSum=0
    for i in range(lr,ur+1):
        check=True
        for j in range(lr,int(i**0.5)+1):
            if i%j==0:
                check=False
                break
        if check:
            if i<2000000:
                primeSum+=i
            else:
                return primeSum

    return primeSum
inp1=int(input('Enter your lower natural number for finding prime numbers:'))
inp2=int(input('Enter your upper natural number for finding prime numbers:'))
if inp2==2:
    print('The prime numer is',2)
elif (inp1>1):
    a=primeSum(inp1,inp2)
    print('The sum of prime numbers  between',inp1,inp2,'is',a)
