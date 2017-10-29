a=input('Enter the name of the file you want to open:\n')
if len(a)<1:
    doc=open('Num.txt','r+')
    print('Opening Num.txt...')
else:
    doc=open(a,'r+')
Prevnum=''
for line in doc:
    x=line.strip()
    number=Prevnum+x
    Prevnum=number
    #print(x)
    #for i in x:
#print(number)
#prod=1
i=0
j=13 #use j=4 for test case..
bigProd=0
bigSeq=''
while (j<=len(number)):
    prod=1
    for m in number[i:j]:
        prod=prod*int(m)
        sequence=number[i:j]
    if prod>bigProd:
        bigProd=prod
        bigseq=sequence
    i+=1
    j+=1


print('The biggest product of 13 adjacent numbers is',bigProd,'the sequence is',bigseq)
