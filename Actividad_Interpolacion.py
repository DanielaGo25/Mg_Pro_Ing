from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

#Valores de la tabla: Razones dimensionales para rangos de giro de la manivela de entrada

deltha_grad = [20,40,60,80,100,120,140,160,180] #Grados de giro de la manivela 
tetha = [170, 160, 150, 140, 130, 120, 110, 100, 90] #Rango angular

ratiosR1 = [0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181] #delthaX/L2
ratiosR2 = [3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800] #L3/L2
ratiosR3 = [2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200] #L1/L2


ratiosV1 = [0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932, 3.232, 3.456] #delthaX/L2
ratiosV2 = [2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125, 2.013, 1.863] #L3/L2
ratiosV3 = [2.075, 2.050, 2.025, 1.975, 1.900, 1.825, 1.750, 1.675, 1.575] #L1/L2

delthaX = 20 #Segmento para el cual se desea determinar las dimensiones del mecanismo

#Interpolaciones con las proporciones 

Inter_tetha_ratiosV1 = lagrange(tetha, ratiosV1)
Inter_tetha_ratiosV2 = lagrange(tetha, ratiosV2)
Inter_tetha_ratiosV3 = lagrange(tetha, ratiosV3)

Inter_tetha_ratiosR1 = lagrange(tetha, ratiosR1)
Inter_tetha_ratiosR2 = lagrange(tetha, ratiosR2)
Inter_tetha_ratiosR3 = lagrange(tetha, ratiosR3)

Inter_grad_ratiosV1 = lagrange(deltha_grad, ratiosV1)
Inter_grad_ratiosV2 = lagrange(deltha_grad, ratiosV2)
Inter_grad_ratiosV3 = lagrange(deltha_grad, ratiosV3)

Inter_grad_ratiosR1 = lagrange(deltha_grad, ratiosR1)
Inter_grad_ratiosR2 = lagrange(deltha_grad, ratiosR2)
Inter_grad_ratiosR3 = lagrange(deltha_grad, ratiosR1)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de rectitud 

L2 = delthaX/Inter_grad_ratiosR1(30)
print('L2: ',L2)

L3 = L2*Inter_grad_ratiosR2(30)
print('L3: ',L3)

L1 = L2*Inter_grad_ratiosR3(30)
print('L1: ',L1)

#Evaluar los polinomios en un intervalo 
t = np.linspace(20,180,200)
y1 = Inter_grad_ratiosR1(t)
y2 = Inter_grad_ratiosR2(t)
y3 = Inter_grad_ratiosR3(t)

#Grafica de las interpolaciones

plt.figure('1')
plt.plot(deltha_grad, ratiosR1, mew=2, label='Datos')
plt.plot(t, y1, label='Interpolacion')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.figure('2')
plt.plot(deltha_grad, ratiosR2, mew=2, label='Datos')
plt.plot(t, y2, label='Interpolación 2')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

plt.figure('3')
plt.plot(deltha_grad, ratiosR2, mew=2, label='Datos')
plt.plot(t, y2, label='Interpolación 3')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()