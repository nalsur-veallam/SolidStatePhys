import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Параметры функции: 
#      a - постоянная решетки
#      N_atoms - количество атомов в системе
#      N_layers - количество слоев атомов в системе
#      N - количество атомов в слое
#      m - масса атома (г/моль - единицы metal LAMMPS)
#      file_name - название считываемого файла

def func(a, N_atoms, N_layers, N, m, file_name):
    
    #Все величины измеряются в единицах metal из LAMMPS
    
    Cp = []
    # fs измеряется в eV/angstrem
    fs = 0
    
    # величина смещения 0.05 - в едеиницах решетки
    const = 0.05 * a

    # Величина вектора k должна лежать в диапазоне от -pi/a до pi/a

    data = pd.read_csv(file_name, delimiter=' ',header = None, index_col=0)

    #Определение силовых постоянных
    for p in range(N_layers):
        if (p != 4):
            for i in range(N_atoms):
                if (data.iloc[i,1] * 10 == p):
                    fs = fs + data.iloc[i, 4]/const
            Cp.append(fs/N)
            fs = 0
            
    # Cp в эВ/ангстрем^2
    Cp_av = []
    Cp_av.append((Cp[3] + Cp[4])/2)
    Cp_av.append((Cp[2] + Cp[5])/2)
    Cp_av.append((Cp[1] + Cp[6])/2)
    Cp_av.append((Cp[0] + Cp[7])/2)
    Cp_av.append(Cp[8])
    
    # Cпектр фононов
    w = []
    k = []
    temp = 0
    r = 0
    k_scaled = []

    k = np.linspace(math.pi/a, -math.pi/a, 100)
    k_scaled = np.linspace(1, -1, 100)
    for counter in range(100):
        r = k[counter]
        
        temp = 0
        for i in range(5):
            temp = temp + Cp_av[i] * (1 - math.cos((i+1) * r * a))
            
        w.append(math.sqrt( 2 * temp / m))
    return Cp, Cp_av, k, k_scaled, w  

Cp_Al, Cp_av_Al, k_Al, k_Al_scaled, w_Al = func(4.04, 500, 10, 50, 26.98, "dump_Al.txt")
Cp_Fe, Cp_av_Fe, k_Fe, k_Fe_scaled, w_Fe = func(2.866, 250, 10, 25, 55.845, "dump_Fe.txt")
Cp_Cu, Cp_av_Cu, k_Cu, k_Cu_scaled, w_Cu = func(3.615, 500, 10, 50, 63.546, "dump_Cu.txt")
Cp_Pb, Cp_av_Pb, k_Pb, k_Pb_scaled, w_Pb = func(4.924, 500, 10, 50, 207.2, "dump_Pb.txt")

p = [-4, -3, -2, -1, 1, 2, 3, 4, 5]

fig, ax = plt.subplots() 
ax.set_xlabel('p')
ax.set_ylabel('Cp, кг/$c^2$')
ax.plot(p, np.array(Cp_Al)*16.02, 'o', label = 'Al')
ax.plot(p, np.array(Cp_Fe)*16.02, 'o',  label = 'Fe')
ax.plot(p, np.array(Cp_Cu)*16.02, 'o',  label = 'Cu')
ax.plot(p, np.array(Cp_Pb)*16.02, 'o', label = 'Pb')
ax.legend()
plt.savefig('Cp_p.pdf')


fig, ax2 = plt.subplots() 
ax2.set_xlabel('k, * $\pi$/a')
ax2.set_ylabel('$\\nu$, $10^{12}$ Гц')
ax2.plot(k_Al_scaled, w_Al, label = 'Al') 
ax2.plot(k_Fe_scaled, w_Fe, label = 'Fe')
ax2.plot(k_Cu_scaled, w_Cu, label = 'Cu')
ax2.plot(k_Pb_scaled, w_Pb, label = 'Pb')
ax2.legend()
ax2.set_title('График зависимости $\\nu$ от k')
plt.savefig('w_k.pdf')
