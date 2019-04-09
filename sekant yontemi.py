#sekant yontemi
def f(x):
    return (x**2-4*x+3)#x1=3,x2=1

x1 = int(input("baslangic degeri : "))
x2 = int(input("bitis degeri : "))

if(f(x1) * f(x2) == 0):
    print("girdiginiz degerlerden biri kok")
else:
    """for i in range(50):
        x3 = x1 - (f(x1)*(x2 - x1)) / (f(x2) - f(x1))#f(x1)*(x2 - x1) / (f(x2) - f(x1))
        x1, x2 = x2, x3
        if(x1 == x2):#if(f(x1) == f(x2)): ikisi de ayni x1==x2 daha verimli
            break
    print(x1, x2,i," adimda")"""
    i=0
    while(abs(f(x2) - f(x1)) > 0.01):
        x3 = x1 - (f(x1)*(x2 - x1)) / (f(x2) - f(x1))#f(x1)*(x2 - x1) / (f(x2) - f(x1))
        x1, x2 = x2, x3
        i+=1
    print(x1, x2, f(x1), f(x2))