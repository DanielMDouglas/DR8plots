#!/usr/bin/python3

from style import *
from utils import *
from dr8TempUtils import *

fig = plt.figure()
ax = fig.gca()

for key in data:

    print (data[key].keys())

    E = np.array(data[key]['Electric Field [kV/cm]']['mean'])
    Eerror = np.array(data[key]['Electric Field [kV/cm]']['err'])
    sheetRes = np.array(data[key]['Sheet Resistance [Ω/sq.]']['mean'])
    sheetResError = np.array(data[key]['Sheet Resistance [Ω/sq.]']['err'])
    
    # V = np.array(data[key]['Voltage [kV]']['mean'])
    # Verror = np.array(data[key]['Voltage [kV]']['err'])
    # L = data[key]['sample_length']
    # W = data[key]['sample_width']
    # current = np.array(data[key]['Current [nA]']['mean'])
    # currentError = np.array(data[key]['Current [nA]']['err'])
    # res = np.array(data[key]['Resistance [Ω]']['mean'])
    # resError = np.array(data[key]['Resistance [Ω]']['err'])
    
    sqrtE = np.sqrt(E)
    sqrtEerror = Eerror*0.5/(sqrtE)
    # # res = V/current
    # sheetRes = res*W/L
    # sheetResError = resError*W/L
    
    
    plt.errorbar(sqrtE,
                 sheetRes,
                 xerr = sqrtEerror,
                 yerr = sheetResError,
                 label = data[key]['label'],
                 color = data[key]['color'],
                 **errorbarKwargs)

plt.axhline(y = 1.e9, ls = '--', color = DUNEdarkOrange)

plt.semilogy()
plt.legend(**legendKwargs)

plt.xlabel(r'$\sqrt{E}$ [(kV/cm)$^{1/2}$]')
plt.ylabel(r'R$_\mathrm{S}$ [$\Omega$/sq.]')

# plt.xlim(-0.05, 2.5)
# plt.ylim(3.e8, 5.e10)

plt.grid()

plt.tight_layout()

plt.savefig('sqrtE_sheetRes_dr8_temp.png', dpi = 300)

# plt.show()
