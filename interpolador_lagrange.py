import numpy as np

n = int(input("Quantidade de pontos já obtidos: "))

x = float(input("Valor para interpolar: "))

X = np.zeros(n)

Y = np.zeros(n)

for i in range(0,n):
        
    X[i] = float(input(f"x[{i}]: "))
    
    Y[i] = float(input(f"y[{i}]: "))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calc_L(x,X,n):
    
    L = np.zeros(n)
    
    for i in range(0,n,1):
        
        prod = 1
        
        for j in range(0,n,1):
            
            if i != j:
                
                prod *= (x - X[j]) / (X[i] - X[j])
                
        L[i] = prod
        
    return L

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def interp_lagrange(x,X,Y,n):

    P = 0
    
    L = calc_L(x, X, n)
    
    for i in range(0,n):
        
        P += Y[i] * L[i]

    return P

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

y_interp = interp_lagrange(x,X,Y,n)

print(f"\nA imagem correspondente ao valor interpolado é, aproximadamente: {y_interp:.5f}")


