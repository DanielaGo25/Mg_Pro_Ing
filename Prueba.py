# Importamos a interpolação de Lagrange do módulo de interpolação do Scipy.
# from scipy.interpolate import lagrange
# Importamos a biblioteca Numpy com um alias para realizar os cálculos.
import numpy as np
# Importamos a biblioteca Sympy para desenvolver a forma algébrica do polinômio.
import sympy as sym
# Importamos a biblioteca Matplotlib com um alias para gráficos.
import matplotlib.pyplot as plt

# Inserimos os dados de teste.
xi = np.array([0, 0.2, 0.3, 0.4])
fi = np.array([1, 1.6, 1.7, 2.0])

# Procedimento.
# Descobrir quantos elementos possui xi.
n = len(xi)
# Atribuímos um caractere X
x = sym.Symbol('x')
# Inicializamos o polinomio
polinomio = 0
# Deslocamos i dentro do intervalo.
for i in range(0,n,1):
    # Para calcular o primeiro termo de Lagrange, é necessário calcular um numerador que é obtido por meio de multiplicações.
    numerador = 1
    denominador = 1
    # O numerador deve percorrer todos os pontos do vetor xi.
    for j in range(0,n,1):
        if (i != j):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
        # Calculamos os termos de lagrange
        termino = (numerador/denominador)*fi[i]
    # Acumulamos os termos.
    polinomio = polinomio + termino
    
# Simplificamos a equação.
polisimple = sym.expand(polinomio)

# Forma lambda do polinômio p(x), referência x e o polinômio que se deseja converter.
px = sym.lambdify(x, polinomio)

# Vetores para graficos.
muestras = 100 # Número qualquer.
a = np.min(xi)
b = np.max(xi)
p_xi = np.linspace(a,b,muestras)
pfi = px(p_xi)

# Saída
print('polinomio')
print(polinomio)
print(' ')
print('polinomio simplificado')
print(polisimple)

# Exemplo com a biblioteca de Lagrange.
# p = lagrange(xi,fi)
# print('polinomio con lagrange')
# print(p)

# Gráfico
plt.plot(xi,fi, 'o')
plt.plot(p_xi,pfi)
plt.show()