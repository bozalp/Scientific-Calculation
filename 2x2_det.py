#determinant 0 kontrol etme
#matris denklem cozumu

def ikilik(x):
    m1 = 0
    m2 = 0
    for i in range(2):
        for j in range(2):
            if(i == 0 and j == 0):
                m1 = (x[i][j] * x[i + 1][j + 1])
            #elif(i == 1 and j == 1):
            else:
                m2 = (x[i][j] * x[j][i])
    sonuc = m1 - m2
    return sonuc

matris = [[2,2],[4,4]]
print(ikilik(matris))

def det(a):
    a.append(a[0]); a.append(a[1]);
    x = 0
    for i in range(0, len(a)-2):
        y=1;        
        for j in range(0, len(a)-2):    
            y *= a[i+j][j]      
        x += y

    p = 0
    for i in range(0, len(a)-2):
        y=1;
        z = 0;
        for j in range(2, -1, -1):  
            y *= a[i+z][j]  
            z+=1        
        z += 1
        p += y  
    return x - p



def dete(a):
   x = (a[0][0] * a[1][1] * a[2][2]) + (a[1][0] * a[2][1] * a[3][2]) + (a[2][0] * a[3][1] * a[4][2])
   y = (a[0][2] * a[1][1] * a[2][0]) + (a[1][2] * a[2][1] * a[3][0]) + (a[2][2] * a[3][1] * a[4][0])
   return x - y

x = [[3,2,2],[4,5,6],[7,8,9]]
print(det(x))
print(dete(x))