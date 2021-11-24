#!/usr/bin/python3

from style import *
from utils import *
from TLMcontUtils import *

testField = np.sqrt(0.5)

widths = []
Rs = []
dRs = []

for item in data:
    W = item["contwid"]
    R = R_model(testField, *item["popt"])
    widths.append(W)
    Rs.append(R)
    dR = dR_model(testField, *item["popt"], item["pcov"])
    dRs.append(dR)
    plt.errorbar(W, R,
                 xerr = dW,
                 yerr = dR,
                 color = item["color"])
    plt.scatter(W, R, color = item["color"])
    
popt, pcov = curve_fit(TLM_model, 
                       widths, Rs,
                       sigma = dRs,
                       p0 = TLM_starting_values,
                       bounds = TLM_optBounds)
print (popt, pcov)

fineLspace = np.linspace(0, 3, 1000)
plt.plot(fineLspace, TLM_model(fineLspace, *popt))

plt.text(1.e-1, 9.8, 'Field Strength = '+str(round(testField**2, 2))+' kV/cm', **textKwargs)
#plt.text(1.e-1, 2.2, 'Field Strength = '+str(round(testField**2, 2))+' kV/cm')
plt.xlabel(r'Contact Patch Width [cm]')
plt.ylabel(r'Sample Resistance [G$\Omega$]')

plt.grid()

#plt.ylim(5, 8)
plt.semilogx()
plt.xlim(3e-2, 4e0)

plt.tight_layout()

plt.savefig('TLM_contact_fit.png', dpi = 300)
