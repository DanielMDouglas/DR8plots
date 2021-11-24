import numpy as np
import os

from style import *

TLMmodelFitFilename = 'fitted_res_models.npy'

if TLMmodelFitFilename in os.listdir('.'):
    data = np.load(TLMmodelFitFilename)
else:
    # data = [{"file": "MSU_TLM_data/TLM_length/sample2.dat",
    #      "length": 1.292,
    #      "label": r'1.292 cm',
    #      "color": DUNEblue},
    #     {"file": "MSU_TLM_data/TLM_length/sample4.dat",
    #      "length": 1.869,
    #      "label": r'1.869 cm',
    #      "color": DUNElightOrange},
    #     {"file": "MSU_TLM_data/TLM_length/sample1.dat",
    #      "length": 2.544,
    #      "label": r'2.544 cm',
    #      "color": DUNEdarkOrange},
    #     {"file": "MSU_TLM_data/TLM_length/sample5.dat",
    #      "length": 3.108,
    #      "label": r'3.108 cm',
    #      "color": DUNEgreen},
    #     {"file": "MSU_TLM_data/TLM_length/sample3.dat",
    #      "length": 3.775,
    #      "label": r'3.775 cm',
    #      "color": DUNEgray},]
    data = [{"file": "MSU_TLM_data/TLM_length/sample2.dat",
             "length": 1.292,
             "label": r'$\sfrac{1}{2}$"',
             "color": DUNEblue},
            {"file": "MSU_TLM_data/TLM_length/sample4.dat",
             "length": 1.869,
             "label": r'$\sfrac{3}{4}$"',
             "color": DUNElightOrange},
            {"file": "MSU_TLM_data/TLM_length/sample1.dat",
             "length": 2.544,
             "label": r'$1$"',
             "color": DUNEdarkOrange},
            {"file": "MSU_TLM_data/TLM_length/sample5.dat",
             "length": 3.108,
             "label": r'$1 \sfrac{1}{4}$"',
             "color": DUNEgreen},
            {"file": "MSU_TLM_data/TLM_length/sample3.dat",
             "length": 3.775,
             "label": r'$1 \sfrac{1}{2}$"',
             "color": DUNEgray},]


dL = 0.025

def R_model(E, R0, E0, a):
    return R0*np.exp(np.sqrt(E0/E) - a*E)

def dR_model(E, R0, E0, a, pcov):
    grad = np.array([R_model(E, R0, E0, a)/R0, # dR/dR0
                     R_model(E, R0, E0, a)/(2*np.sqrt(E*E0)), # dR/dE0
                     R_model(E, R0, E0, a)*E # dR/da
                    ])
    return np.sqrt(np.dot(grad, np.dot(pcov, grad)))

res_starting_values = (1, 1, 1)
res_optBounds = ([1e-5, 1e-1, 1e-3],[1e1, 50, 1e3])

def TLM_model(L, m, b):
    return m*L + b

TLM_starting_values = (4, 0)
TLM_optBounds = ([0, -10], [20, 10])
