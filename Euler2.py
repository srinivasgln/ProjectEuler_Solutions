def fibevn(a,b):
    i=1
    loc=list()
    loc.append(a)
    loc.append(b)
    inp=int(input('enter the end limit for final number in fibonacci series\t'))
    while True:
        fbn=loc[i]+loc[i-1]
        if (fbn<=inp):
            loc.append(fbn)
            i=i+1
        else:
            return loc
            break
fn=int(input('enter the first number of the fibonacci series\n'))
sn=int(input('enter the second number of the fibonacci series\n'))
fs=fibevn(fn,sn)
print(fs)
tot=0
for i in fs:
  if i%2==0:
      #print('the even no being conisered is',i)
      tot=tot+i
      #print(' even total thus far', tot)

print('the total sum of even integers in the fibonacci series is\t',tot)
