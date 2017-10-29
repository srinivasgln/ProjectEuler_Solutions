def propdiv(n):
    div=[]
    for i in range(1,n):
        if n%i==0:
            div.append(i)
    if sum(div)==n:
        print('The numnber is perfect number as its sum equals',sum(div))
    elif sum(div)<n:
        print('The numnber is deficient no as its sum equals',sum(div))
    elif sum(div)>n:
        print('The numnber is abundant number as its sum equals',sum(div))
    return div

a=int(input('Enter the number for which you like to find the proper divisors:'))
print('The proper divisors are',propdiv(a))
