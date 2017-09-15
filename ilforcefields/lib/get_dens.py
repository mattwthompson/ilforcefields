import os

import mbuild as mb
from pkg_resources import resource_filename
import json

def get_dens(il_name):
    filename = resource_filename('ilforcefields', 'lib/dens.json')
    with open(filename) as fi:
        dens = json.load(fi)
    return dens[il_name.lower()]
