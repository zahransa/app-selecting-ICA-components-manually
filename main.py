import os
import mne
import json
import matplotlib.pyplot as plt
# Load brainlife config.json
with open('config.json','r') as config_f:
    config = json.load(config_f)


fname = config['fif']
ica=mne.preprocessing.read_ica(fname, verbose=None)
ica.exclude = [0, 1]
#ica.exclude = config['exclude']
print('test')
#
ica.save('out_dir/ica.fif')