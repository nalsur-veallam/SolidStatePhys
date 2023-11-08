import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


lattice = 2.86
delta = 0.01
C = [0] * 5
data = np.loadtxt("dump.fe",skiprows=9,max_rows=500)
for i in range(500):
    if(data[i][2] >= 0.5):
        C[int(data[i][2] * 10 - 5)] = data[i][5]
print(np.array(C))
C = np.array(C)/(delta) * 1.602 * 10
print(C)


fig = plt.figure(figsize=(12,8))
x = np.linspace(1,5,5)
plt.plot(x,C, "ok")
plt.title("Силовые постоянные для Fe")
plt.ylabel(r"$C_p, 10^3 дин/см$")
plt.xlabel(r"Плоскость $p$")
plt.grid()
plt.savefig("forcesFe.pdf")

def disp(x):
    res = 0
    for p, C_p in enumerate(C):
        res += (2.0 * C_p * (1.0 - np.cos((p+1) * 2.0 * np.pi * x)))
    return (res/55.8 * 6e23 * 1e3)**0.5 / 2.0 / np.pi * 1e-12
fig = plt.figure(figsize=(12,8))
x = np.linspace(0,0.5,1000)
y = [0] * 1000
for i, x_i in enumerate(x):
    y[i] = disp(x_i)
plt.title(r"Фононный спектр для Fe. Продольная волна, направление [100]")
plt.plot(x, y, "-k")
plt.ylabel(r"$\nu, TГц$")
plt.xlabel(r"ka/2$\pi$")
plt.grid()
plt.savefig("spectrumFe.pdf")
