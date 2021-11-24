from json import decoder
import yaml

dec = decoder.JSONDecoder()

data = {'ladder':   {'datafile': './alt_design_data/dr8_ladder_ln2.json',
                     'configfile': './alt_design_data/dr8_ladder_ln2.yaml',
                     'label': r'Ladder'},
        'full':     {'datafile': './alt_design_data/dr8_ln2.json',
                     'configfile': './alt_design_data/dr8_ln2.yaml',
                     'label': r'Full'},
        'zebra 50': {'datafile': './alt_design_data/dr8_zebra1_ln2.json',
                     'configfile': './alt_design_data/dr8_zebra1_ln2.yaml',
                     'label': r'Zebra 50\%'},
        'zebra 75': {'datafile': './alt_design_data/dr8_zebra2_ln2.json',
                     'configfile': './alt_design_data/dr8_zebra2_ln2.yaml',
                     'label': r'Zebra 75\%'},
        }

for item in data.values():
    raw_text = open(item['datafile']).read()
    data_content = dec.decode(raw_text)

    config = yaml.load(open(item['configfile']), Loader=yaml.FullLoader)

    item.update(data_content)
    item.update(config)
