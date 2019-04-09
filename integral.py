#kisakenar integral

def f(x):
    return (x**2)
    
x1 = 4
x2 = 6
#n -> araligin kac parcaya bolunecegi
n = 1000
h = (x2 - x1) / n
integral = 0

for i in range(n):
    integral += f(x1 + i * h) * h

print(integral)

integral2 = 0
for i in range(1, n + 1):
    integral2 += f(x1 + i * h) * h

print(integral2)