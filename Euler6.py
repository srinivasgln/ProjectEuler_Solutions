def sumsq(lr,ur):
    tot1=0
    for i in range(lr,ur+1):
        sq1=i*i
        tot1+=sq1
    return tot1
def sq_sum(lr,ur):
    sm=0
    for i in range(lr,ur+1):
        sm+=i
    return sm**2
inp1=int(input('Enter the lower range :'))
inp2=int(input('Enter the upper range :'))
result=sq_sum(inp1,inp2)-sumsq(inp1,inp2)
print('The difference between the sum of the squares of the natural numbers and the square of their sum between',
        inp1,'and',inp2,'is',result)
