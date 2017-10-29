def factSum(a):
    prod=1
    for i in range(1,a+1):
        prod*=i
    sm_fact=0
    for j in str(prod):
        sm_fact+=int(j)
    return prod,sm_fact
x=int(input('Enter the number for which you like to find factorial !:'))
ft,ft_sm=factSum(x)
print('The factorial is',ft,'The sum of the factorial is',ft_sm)
