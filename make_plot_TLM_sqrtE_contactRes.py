#!/usr/bin/python3

from style import *
from utils import *
from TLMutils import *

testFields = np.linspace(0.1, 1, 500)
Rcs = []
dRcs = []

for testField in testFields:
    lengths = []
    Rs = []
    dRs = []

    for item in data:
        L = item["length"]
        #R = R_model(testField, *item["popt"])
        R = R_model(np.sqrt(testField), *item["popt"])
        lengths.append(L)
        Rs.append(R)
        #dR = dR_model(testField, *item["popt"], item["pcov"])
        dR = dR_model(np.sqrt(testField), *item["popt"], item["pcov"])
        dRs.append(dR)
    
    popt, pcov = curve_fit(TLM_model, 
                           lengths, Rs,
                           sigma = dRs,
                           #absolute_sigma = True,
                           p0 = TLM_starting_values,
                           bounds = TLM_optBounds)
    Rcs.append(0.5*popt[1])
    dRcs.append(0.5*pcov[1][1])
        
lower_bound = [R - dR for R, dR in zip(Rcs, dRcs)]
upper_bound = [R + dR for R, dR in zip(Rcs, dRcs)]
    
plt.plot(testFields, Rcs, color = DUNEdarkOrange)
plt.fill_between(testFields, lower_bound, upper_bound, alpha = 0.5, color = DUNElightOrange)

#plt.semilogy()
plt.grid()

plt.xlabel(r'$\sqrt{E}$ [(kV/cm)$^{1/2}$]')
plt.ylabel(r'$R_C$ [G$\Omega$]')

plt.tight_layout()

plt.savefig('TLM_length_contactRes.png', dpi = 300)
