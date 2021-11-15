from json import decoder

dec = decoder.JSONDecoder()

data = {'ladder':   {'infile': './alt_design_data/dr8_ladder_ln2.json',
                     'label': r'Ladder (LN$_2$)'},
        'full':     {'infile': './alt_design_data/dr8_ln2.json',
                     'label': r'Full (LN$_2$)'},
        'zebra 50': {'infile': './alt_design_data/dr8_zebra1_ln2.json',
                     'label': r'Zebra 50\% (LN$_2$)'},
        'zebra 75': {'infile': './alt_design_data/dr8_zebra2_ln2.json',
                     'label': r'Zebra 75\% (LN$_2$)'},
        }

for item in data.values():
    raw_text = open(item['infile']).read()
    json = dec.decode(raw_text)

    item.update(json)
