import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

DUNEblue = '#7FAED5'
DUNElightOrange = '#F19E54'
DUNEdarkOrange = '#F0652B'
DUNEgreen = '#8ACA6F'
DUNEgray = '#626466'
DUNEyellow = '#FBD03F'
DUNEpurple = '#5B3069'
DUNElightPurple = '#8C6E96'
DUNEcyan = '#42C2A8'
DUNEpink = '#F7AEC2'

DUNEcolors = [DUNEblue,
              DUNElightOrange,
              DUNEdarkOrange,
              DUNEgreen,
              DUNEgray,
              DUNEyellow,
              DUNEpurple,
              DUNElightPurple,
              DUNEcyan,
              DUNEpink]

# matplotlib.rc('font', family = 'FreeSerif', size = 16, weight = 'bold')
matplotlib.rc('font', family = 'FreeSerif', size = 24, weight = 'bold')
matplotlib.rc('text', usetex = True)
matplotlib.rc('axes', prop_cycle = matplotlib.cycler(color = DUNEcolors))
matplotlib.rc('figure', figsize = (6.0, 4.8))

errorbarKwargs = {'ls': 'none',
                  'fmt': 'o',
                  'ms': 2}

legendKwargs = {'frameon': False,
                'prop': {'size': 18}}
