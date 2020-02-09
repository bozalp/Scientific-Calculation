#doğruya yaklaştırma
#[i**2 for i in x]-->[1, 4, 9, 16, 36, 49, 81]
x = [1, 2, 3, 4, 6, 7, 9]
#y = [3, 5.5, 7.2, 8.9, 13.4, 15, 19]
y = [3, 5, 7, 9, 13, 15, 19]

xi_yi = 0

for i in range(len(x)):
    xi_yi += x[i] * y[i]
    
a1 = (len(x) * xi_yi - sum(x) * sum(y)) / (len(x) * sum([i**2 for i in x]) - sum(x)**2)

a0 = (sum(y) - a1 * sum(x)) / len(x)

print(a0, a1)
print(a0 + a1 * 5)

"""
xiyi = sum([x[i]*y[i] for i in range(len(x))])

a1 = (len(x)*xiyi - sum(x)*sum(y)) / (len(x)*sum([i**2 for i in x]) - sum(x)**2)
a0 = (sum(y) - a1*sum(x))/len(x)"""
#kısası 

