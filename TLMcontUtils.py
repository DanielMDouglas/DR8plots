from style import *
import os

def R_model(E, R0, E0, a):
    return R0*np.exp(np.sqrt(E0/E) - a*E)

def dR_model(E, R0, E0, a, pcov):
    grad = np.array([R_model(E, R0, E0, a)/R0, # dR/dR0
                     R_model(E, R0, E0, a)/(2*np.sqrt(E*E0)), # dR/dE0
                     R_model(E, R0, E0, a)*E # dR/da
                    ])
    return np.dot(grad, np.dot(pcov, grad))

res_starting_values = (1.5, 3.5, 1.5)
res_optBounds = ([1e-5, 1e-1, 1e-3],[1e2, 50, 1e3])

@np.vectorize
def TLM_model(L, b):
    return b

TLM_starting_values = (2)
TLM_optBounds = ([0], [100])

TLMcontModelFitFilename = 'fitted_res_models_contact_width.npy'

if TLMcontModelFitFilename in os.listdir('.'):
    data = np.load(TLMcontModelFitFilename)
else:
    data = [{"file": "MSU_TLM_data/TLM_contact/sample1.dat",
             "contwid": 2.582,
             "length": 2.865,
             # "label": r'2.582 cm',
             "label": r'2.58 cm',
             "color": DUNEdarkOrange},
            {"file": "MSU_TLM_data/TLM_contact/sample2.dat",
             "contwid": 1.904,
             "length": 2.865,
             # "label": r'1.904 cm',
             "label": r'1.90 cm',
             "color": DUNEblue},
            {"file": "MSU_TLM_data/TLM_contact/sample3.dat",
             "contwid": 1.263,
             "length": 2.865,
             # "label": r'1.263 cm',
             "label": r'1.26 cm',
             "color": DUNEgray},
            {"file": "MSU_TLM_data/TLM_contact/sample4.dat",
             "contwid": 0.628,
             "length": 2.865,
             # "label": r'0.628 cm',
             "label": r'0.63 cm',
             "color": DUNElightOrange},
            {"file": "MSU_TLM_data/TLM_contact/sample5.dat",
             "contwid": 0.301,
             "length": 2.865,
             # "label": r'0.301 cm',
             "label": r'0.30 cm',
             "color": DUNEgreen},
            {"file": "MSU_TLM_data/TLM_contact/sample6.dat",
             "contwid": 0.100,
             "length": 2.865,
             # "label": r'0.100 cm',
             "label": r'0.10 cm',
             "color": DUNEpink},
            {"file": "MSU_TLM_data/TLM_contact/sample7.dat",
             "contwid": 0.064,
             "length": 2.865,
             # "label": r'0.064 cm',
             "label": r'0.06 cm',
             "color": DUNElightPurple}]

dL = 0.025
dW = 0.025
