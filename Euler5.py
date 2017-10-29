ls=1
a=True
while a:
    count=0
    for i in range(1,21):
        if ls%i==0:
            count=count+1
            if count==20: # change the counter based on the for range []
                a=False
                break
            continue
        else:
            ls=ls+1
            break
print('The smallest multiple of 1 to 20 is',ls)
