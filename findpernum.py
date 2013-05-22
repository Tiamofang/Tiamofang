#find the perfect num!
#从一定范围内找出其中的完全数;
#1.需要一个循环,来对这个范围的数字进行遍历 Thenum=2, Thenum+=1
#2.对遍历中的每个数字,进行判断Thenum的因数和sumdivisor ==?
#3.如何求sumdivisor,sumdivisor=sumdivisor+divisor
#4.使用循环和判断来确定divisor的(因数)

Topnumstr=raw_input("Please input the upper number for the range:")
Topnum=int(Topnumstr)
Thenum=2
while Thenum<=Topnum:
    divisor=1
    sumdivisor=0
    while divisor<Thenum:
        if Thenum%divisor==0:
            sumdivisor=sumdivisor+divisor
        divisor+=1
    if sumdivisor==Thenum:
        print Thenum,"is a perfectnum!"
    Thenum+=1
    

