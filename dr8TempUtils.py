from style import *

from json import decoder
import yaml

dec = decoder.JSONDecoder()

data = {'lar':   {'datafile': './dr8_temp_data/dr8_lar.json',
                  'label': r'LAr',
                  'color': DUNEblue},
        'ln2':     {'datafile': './dr8_temp_data/dr8_ln2.json',
                    'label': r'LN$_2$',
                    'color': DUNElightOrange},
        'rt': {'datafile': './dr8_temp_data/dr8_rt.json',
               'label': r'Room temp.',
               'color': DUNEgreen},
        }

for item in data.values():
    raw_text = open(item['datafile']).read()
    data_content = dec.decode(raw_text)

    item.update(data_content)
