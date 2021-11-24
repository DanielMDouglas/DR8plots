#!/usr/bin/python3

from style import *
from utils import *
from TLMcontUtils import *

### MSU TLM Plot 2: sqrt(E) vs. resistance

fig = plt.figure()
ax = fig.gca()

for item in data:
    if 'cut' in item:
        V, dV, I, dI = np.loadtxt(item["file"], 
                                  delimiter = ',', 
                                  skiprows = 2)[item["cut"]:].T
    else:
        V, dV, I, dI = np.loadtxt(item["file"], 
                                  delimiter = ',', 
                                  skiprows = 2).T
    
    V /= 1000 # voltage in kV
    dV /= 1000
    
    I /= 1000 # current in mA
    dI /= 1000
    
    L = item["length"]
    
    E = V/item["length"]
    dE = E*quadr_sum(dV/V, dL/L)
    
    sqrtE = np.sqrt(E)
    dSqrtE = sqrtE*quadr_sum(0.5*dV/V, 0.5*dL/L)
    
    R = V/I # resistance in MOhm
    dR = R*quadr_sum(dV/V, dI/I)
    
    R *= 1.e-3 # resistance in GOhm
    dR *= 1.e-3
    
    ax.errorbar(sqrtE, R,
                xerr = dSqrtE,
                yerr = dR,
                ls = "none",
                fmt = 'o',
                ms = 2,
                label = item["label"],
                color = item["color"])
    
    #print (starting_values)
    #print (R_model(sqrtE, *starting_values))
    popt, pcov = curve_fit(R_model, 
                           sqrtE[1:], R[1:], 
                           sigma= dR[1:],
                           #absolute_sigma = True,
                           p0 = res_starting_values,
                           bounds = res_optBounds)
    
    #print (item["label"])
    #print (popt, pcov)
    if np.any(pcov[np.isfinite(pcov)]):
        print(item["label"], popt, pcov)
        fineSqrtE = np.linspace(0.25, 1.5, 1000)
        plt.plot(fineSqrtE, 
                 R_model(fineSqrtE, *popt),
                 color = item["color"])
        item["popt"] = popt
        item["pcov"] = pcov
    
ax.legend(ncol = 1, loc = 'upper right',  **legendKwargs)
ax.set_xlabel(r'$\sqrt{E}$ [(kV/cm)$^{|1/2}$]')
ax.set_ylabel(r'R [G$\Omega$]')

plt.grid()
#plt.plot(fineSqrtE, R_model(fineSqrtE, *starting_values))

#ax.set_ylim(1e-1 ,1e3)

plt.xlim(0.2, 1.9)
# plt.ylim(1., 5.e2)
plt.semilogy()  

plt.tight_layout()

plt.savefig('TLM_contact_resistance.png', dpi = 300)

np.save(TLMcontModelFitFilename, data)
