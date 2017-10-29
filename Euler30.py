def digit_power(n):
    #for i in range(lr,ur+1):
    s=str(n)
    power=5 #len(s)
    sm=0

    for i in s:
        sm=sm+(int(i)**power)
    if sm==n:
        print('The given number',n,'can be written as the sum of fourth powers of their digits')
        return n



    #else:
    #    print('The given number cannot be written as the sum of fourth powers of their digits')


#a=int(input('Enter a number:'))
#digit_power(a)
x=int(input('Enter lower range:'))
y=int(input('Enter upper range:'))
dig_pw=[]
for m in range(x,y+1):
    res=digit_power(m)
    if type(res)==int:
        dig_pw.append(res)
print('The numbers found are',dig_pw,'and its sum are',sum(dig_pw))
