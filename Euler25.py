def fibno(n,leng,limit=None):
    fn_1=1
    fn_2=1
    check=True
    fibnocci=[]
    fibnocci.append(n)
    fibnocci.append(n)
    count=2
    while check:
        fibnum=fn_1+fn_2
        fn_2=fn_1
        fn_1=fibnum
        fibnocci.append(fibnum)
        count+=1
        if len(str(fibnum))==leng:
            check=False

    return fibnum,fibnocci,count
a=int(input('Enter the starting number of your fibnocci series:'))
b=int(input('Enter the digits of nth term of your fibnocci series upto which you like to find:'))
fn,series_fib,series_leng=fibno(a,b,None)
print('The last term of your fibnocci series is ',fn,'having the index of', series_leng)
