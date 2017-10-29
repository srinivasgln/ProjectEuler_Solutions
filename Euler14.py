def collatz(n):
    check=True
    count=0
    while check:
        count+=1
        if n>1:
            if n%2==0:
                n=n/2
            else:
                n=(3*n)+1
        if n==1:
            count+=1
            check=False
    return count
a=int(input('Enter the end range / number to find length of collaztz sequence:'))
#print('the length of collatz sequence is ',collatz(a))

bigcollatz=0
bigno=0
for i in range(1,a+1):
    r=collatz(i)
    if r>bigcollatz:
        bigcollatz=r
        bigno=i
print('the number with largest collatz sequence is',bigno,'and its sequence length is',bigcollatz)
