# Base para la solución del Laboratorio 4

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatorias X y Y, se asigna una media de 0 y una varianza de 15 siguiendo el problema 2
vaX = stats.norm(0, np.sqrt(15))
vaY = stats.norm(0, np.sqrt(15))

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio Z(t) con N realizaciones
N = 15
Z_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso Z(t) (X y Y independientes) (se asigna una velocidad angular de pi)
for i in range(N):
	X = vaX.rvs()
	Y = vaY.rvs()
	z_t = X*np.cos(np.pi*t) + Y*np.sin(np.pi*t)
	Z_t[i,:] = z_t
	plt.plot(t, z_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(Z_t[:,i]) for i in range(len(t))]
plt.plot(t, P, '-.', lw=6)

# Se imprime la suma de P para demostrar que se llega a cero 
print(np.sum(P))

# Graficar el resultado teórico del valor esperado
E = t*0
plt.plot(t, E, '-.', lw=6)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $Z(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(Z_t[n,:], np.roll(Z_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
Rxx = 15 * np.cos(np.pi*taus)

# Gráficas de correlación para cada realización y la
plt.plot(taus, Rxx, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{WW}(\tau)$')
plt.legend()
plt.show()