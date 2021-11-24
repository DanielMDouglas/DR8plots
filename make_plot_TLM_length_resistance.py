#!/usr/bin/python3

from style import *
from utils import *
from TLMutils import *

starting_values = (4, 0)
optBounds = ([0, -10], [20, 10])

testField = np.sqrt(0.5)

lengths = []
Rs = []
dRs = []

for item in data:
    L = item["length"]
    R = R_model(testField, *item["popt"])
    lengths.append(L)
    Rs.append(R)
    dR = dR_model(testField, *item["popt"], item["pcov"])
    dRs.append(dR)
    print (L, R, dR)
    plt.errorbar(L, R,
                 xerr = dL,
                 yerr = dR,
                 color = item["color"],
                 **errorbarKwargs)
    plt.scatter(L, R, color = item["color"])

popt, pcov = curve_fit(TLM_model, 
                       lengths, Rs,
                       sigma = dRs,
                       #absolute_sigma = True,
                       p0 = starting_values,
                       bounds = optBounds)
print (popt, pcov)
print ("contact resistance at 500 V/cm = ", popt[1], "+/-", np.sqrt(pcov[1][1]))

fineLspace = np.linspace(0, 4, 1000)
plt.plot(fineLspace, TLM_model(fineLspace, *popt))

plt.text(0, 6, 'Field Strength = '+str(round(testField**2, 2))+' kV/cm', **textKwargs)

# plt.text(-.8, -2, '(a)', **plotLabelTextKwargs)

plt.xlabel(r'Sample Length [cm]')
plt.ylabel(r'Sample Resistance [G$\Omega$]')

plt.tight_layout()

plt.savefig('TLM_length_TLMfit.png', dpi = 300)
