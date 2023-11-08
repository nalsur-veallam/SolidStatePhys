import numpy as np
import pylab as plt
from scipy.integrate import simpson

e = 1.60217663 * 10**(-19)
k = 8.617333 * 10**(-5)
kb = 1.380649 * 10**(-23)


def func(E, mu,T):
    return 1/(np.cosh((E-mu)/k/T)+1)

def int_func_0(E, mu, T):
    return E**(3/2) * func(E, mu,T)

def int_func_1(E, mu, T):
    return E**(3/2) * (E - mu) * func(E, mu, T)

def get_seebek(mu, T, N=50000, Nkt=30):
    E_min = mu - Nkt*k*T
    E_max = mu + Nkt*k*T
    dE = (E_max-E_min)/N
    E = np.arange(E_min, E_max+dE, dE)
    I_1 = simpson(int_func_1(E, mu, T), E)
    I_0 = simpson(int_func_0(E, mu, T), E)
    S = -I_1/I_0/T * 10**6
    return S
    
    
mu = 11.7 # эв
T = 300

T_arr = np.linspace(200, 420, 30)
S_arr = np.zeros(len(T_arr))
for i in range(len(T_arr)):
    S_arr[i] = get_seebek(mu, T_arr[i])
    
fig, axs = plt.subplots()  
plt.plot(T_arr, S_arr, '-o')
plt.xlabel('T, K')
plt.ylabel('S, мкВ/К')
plt.grid()
plt.show()
fig.savefig('plot_T.pdf')


E_arr = np.linspace(0.1, 2, 50)
S_arr = np.zeros(len(E_arr))
for i in range(len(E_arr)):
    S_arr[i] = get_seebek(mu*E_arr[i], T)

fig, axs = plt.subplots()
plt.plot(E_arr, S_arr, '-o')
plt.xlabel('$\mu$, $E_F$')
plt.ylabel('S, мкВ/К')
plt.grid()
plt.show()
fig.savefig('plot.pdf')


print(get_seebek(mu, T))
