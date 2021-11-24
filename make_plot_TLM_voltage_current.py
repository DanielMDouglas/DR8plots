#!/usr/bin/python3

from style import *
from utils import *
from TLMutils import *

### MSU TLM Plot 1: voltage vs. current

fig = plt.figure()
ax = fig.gca()

for item in data:
    V, dV, I, dI = np.loadtxt(item["file"], 
                              delimiter = ',', 
                              skiprows = 1).T
    
    V /= 1000 # voltage in kV
    dV /= 1000
    
    I /= 1000 # current in mA
    dI /= 1000
    
    ax.errorbar(V, I,
                xerr = dV,
                yerr = dI,
                label = item["label"],
                **errorbarKwargs)
    
ax.legend(ncol = 1, **legendKwargs)
ax.set_xlabel(r'Voltage [kV]')
ax.set_ylabel(r'Current [mA]')

# plt.text(-1.5, -0.01, '(a)', **plotLabelTextKwargs)
plt.tight_layout()

plt.savefig('TLM_length_current.png', dpi = 300)
