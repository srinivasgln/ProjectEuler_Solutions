def power_seq(base_low,base_upper,power_low,power_upper):
    loc=list()
    for m in range(base_low,base_upper+1):
        for n in range(power_low,power_upper+1):
            r=m**n
            if r not in loc:
                loc.append(r)
    return loc

lb=int(input('Enter your lower base:'))
ub=int(input('Enter your upper base:'))
lp=int(input('Enter your lower power:'))
up=int(input('Enter your upper power:'))
resul=power_seq(lb,ub,lp,up)
print('The number of distinct entries in the sequence is',len(resul))
#print('The unique numbers are',resul)
