def powdgt(a,b):
    if type(a)==int and type (b)==int:
        r=a**b
        #to find the sum of all digits in the result:
        st=str(r)
        l=0
        for i in st:
            l+=int(i)
    return l
inp=input('Enter the base and the power separated by comma:')
x,y=inp.split(',')
x=int(x)
y=int(y)
print('The sum of digits of',x,'power',y,'is',powdgt(x,y))
#'The sum of digits of {0} power {1} is {2}'.format(x,y,powdgt(x,y))
