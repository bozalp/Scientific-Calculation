#kok bulma-yariya bolme ile
#%1 için hangisi daha hızlı sonuc döndürür

def f(x):
    return (x ** 2 - 4 * x + 3)#(x-1).(x-3)--> x1=1 x2=3
    

x1 = int(input("Baslangic Tahmini : "))
x2 = int(input("Bitis Tahmini : "))

if(f(x1) * f(x2) == 0):
    print("Tahminlerinizden biri denklemin kokudur")
elif(f(x1) * f(x2) > 0):
    print("Girdiginiz aralikta tek sayida kok yoktur")
else:
    for i in range(100):
        xr = (x1 + x2) / 2
        if(f(xr) == 0):
            print("Kok bulundu ->", xr,"---", i+1," adımda bulundu")
            break
        elif(f(x1) * f(xr) < 0):
            x2 = xr
        else:
            x1 = xr
        print(xr)