import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import memory_buffer_doubling as memb
from matplotlib import ticker, cm



"""
Goal of this program: 
- computes waiting times for different swapping_probabilities and distributions of memory_numbers.
- make plots: waiting_time(swapping_probability) for different memory distributions
"""

"""simulation parameters"""
memory_numbers = [2,1,1,2,2,1,1,2]
#generation_probability=0.01
#swapping_probability=0.5
number_of_repetitions=100 
datap = np.linspace(0.1,1,10)  #vektoren in Matrix
dataa = np.linspace(0.1,1,10)



Z = np.array([np.array([memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=p,
                          swapping_probability=a,
                          number_of_repetitions=number_of_repetitions)[0] for p in datap])for a in dataa])





# Automatic selection of levels works; setting the
# log locator tells contourf to use a log scale:
fig, ax = plt.subplots()
cs = ax.contourf(datap, dataa, Z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

# Alternatively, you can manually set the levels
# and the norm:
# lev_exp = np.arange(np.floor(np.log10(z.min())-1),
#                    np.ceil(np.log10(z.max())+1))
# levs = np.power(10, lev_exp)
# cs = ax.contourf(X, Y, z, levs, norm=colors.LogNorm())

plt.xlabel('generation probability $p$')
plt.ylabel(r'swapping probability $a$')

cbar = fig.colorbar(cs)
plt.title('memory numbers=%s, number_of_repetitions=%i' %(memory_numbers,number_of_repetitions))
plt.show()
