from scipy.interpolate import lagrange
from scipy.interpolate import InterpolatedUnivariateSpline
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

#Interpolaciones empleando lagrange 
print('\nInterpolaciones empleando lagrange: ')
Inter_grad_ratiosV1 = lagrange(deltha_grad, ratiosV1)
Inter_grad_ratiosV2 = lagrange(deltha_grad, ratiosV2)
Inter_grad_ratiosV3 = lagrange(deltha_grad, ratiosV3)

Inter_grad_ratiosR1 = lagrange(deltha_grad, ratiosR1)
Inter_grad_ratiosR2 = lagrange(deltha_grad, ratiosR2)
Inter_grad_ratiosR3 = lagrange(deltha_grad, ratiosR3)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de rectitud con 30 grados
print('\nValores de L1, L2 yL3 en criterio de rectitud con 30 grados: ')
L2 = delthaX/Inter_grad_ratiosR1(30)
print('\nL2: ',L2)
L3 = L2*Inter_grad_ratiosR2(30)
print('L3: ',L3)
L1 = L2*Inter_grad_ratiosR3(30)
print('L1: ',L1)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de rectitud con 55 grados
print('\nValores de L1, L2 yL3 en criterio de rectitud con 55 grados: ')
L_2 = delthaX/Inter_grad_ratiosR1(55)
print('\nL_2: ',L_2)
L_3 = L_2*Inter_grad_ratiosR2(55)
print('L_3: ',L_3)
L_1 = L_2*Inter_grad_ratiosR3(55)
print('L_1: ',L_1)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de velocidad con 30 grados
print('\nValores de L1, L2 yL3 en criterio de velocidad con 30 grados: ')
l2 = delthaX/Inter_grad_ratiosV1(30)
print('\nL2: ',l2)
l3 = l2*Inter_grad_ratiosV2(30)
print('L3: ',l3)
l1 = l2*Inter_grad_ratiosV3(30)
print('L1: ',l1)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de velocidad con 55 grados
print('\nValores de L1, L2 yL3 en criterio de velocidad con 55 grados: ')
l_2 = delthaX/Inter_grad_ratiosV1(55)
print('\nL2: ',l_2)
l_3 = l_2*Inter_grad_ratiosV2(55)
print('L3: ',l_3)
l_1 = l_2*Inter_grad_ratiosV3(55)
print('L1: ',l_1)

#Evaluar los polinomios en un intervalo 
t = np.linspace(20,180,200)
y1 = Inter_grad_ratiosR1(t)
y2 = Inter_grad_ratiosR2(t)
y3 = Inter_grad_ratiosR3(t)

x1 = Inter_grad_ratiosV1(t)
x2 = Inter_grad_ratiosV2(t)
x3 = Inter_grad_ratiosV3(t)

#Gráfica de las interpolaciones

#Interpolaciones empleando Splines
print('\nInterpolaciones empleando Splines: ')
Inter_ratiosR1 = InterpolatedUnivariateSpline(deltha_grad, ratiosR1)
Inter_ratiosR2 = InterpolatedUnivariateSpline(deltha_grad, ratiosR2)
Inter_ratiosR3 = InterpolatedUnivariateSpline(deltha_grad, ratiosR3)

Inter_ratiosV1 = InterpolatedUnivariateSpline(deltha_grad, ratiosV1)
Inter_ratiosV2 = InterpolatedUnivariateSpline(deltha_grad, ratiosV2)
Inter_ratiosV3 = InterpolatedUnivariateSpline(deltha_grad, ratiosV3)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de rectitud con 30 grados
print('\nValores de L1, L2 yL3 en criterio de rectitud con 30 grados: ')
l_1_2 = delthaX/Inter_ratiosR1(30)
print('\nL2: ',l_1_2)
l_1_3 = l_1_2*Inter_ratiosR2(30)
print('L3: ',l_1_3)
l_1_1 = l_1_2*Inter_ratiosR3(30)
print('L1: ',l_1_1)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de rectitud con 55 grados
print('\nValores de L1, L2 yL3 en criterio de rectitud con 55 grados: ')
l_2_2 = delthaX/Inter_ratiosR1(55)
print('\nL2: ',l_2_2)
l_2_3 = l_2_2*Inter_ratiosR2(55)
print('L3: ',l_2_3)
l_2_1 = l_2_2*Inter_ratiosR3(55)
print('L1: ',l_2_1)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de velocidad con 30 grados
print('\nValores de L1, L2 yL3 en criterio de velocidad con 30 grados: ')
L_1_2 = delthaX/Inter_ratiosV1(30)
print('\nL2: ',L_1_2)
L_1_3 = L_1_2*Inter_ratiosV2(30)
print('L3: ',L_1_3)
L_1_1 = L_1_2*Inter_ratiosV3(30)
print('L1: ',L_1_1)

#Determinar los valores de L2, L3 y L1, al despejar las proporciones en el criterio de velocidad con 55 grados
print('\nValores de L1, L2 yL3 en criterio de velocidad con 55 grados: ')
L_2_2 = delthaX/Inter_ratiosV1(55)
print('\nL2: ',L_2_2)
L_2_3 = L_2_2*Inter_ratiosV2(55)
print('L3: ',L_2_3)
L_2_1 = L_2_2*Inter_ratiosV3(55)
print('L1: ',L_2_1)

#Evaluar los polinomios en un intervalo 
y_1 = Inter_ratiosR1(t)
y_2 = Inter_ratiosR2(t)
y_3 = Inter_ratiosR3(t)

x_1 = Inter_ratiosV1(t)
x_2 = Inter_ratiosV2(t)
x_3 = Inter_ratiosV3(t)

#Gráfica de las interpolaciones