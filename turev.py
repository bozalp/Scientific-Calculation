
def f(x):
    return (2 * x ** 3 + x - 3)

def ileri_sonlu_farkli_turev(x0, h):
    sonuc = (-f(x0) + f(x0 + h)) / h
    return sonuc

def geri_sonlu_farkli_turev(x0, h):
    sonuc = (f(x0) - f(x0 - h)) / h
    return sonuc

def merkezi_sonlu_farkli_turev(x0, h):
    sonuc = (f(x0 + h) - f(x0 - h)) / (2 * h)
    return sonuc

print(ileri_sonlu_farkli_turev(2, 0.1))
print(geri_sonlu_farkli_turev(2, 0.1))
print(merkezi_sonlu_farkli_turev(2, 0.1))
