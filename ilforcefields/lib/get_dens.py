import inspect
import os

import mbuild as mb
from pkg_resources import resource_filename
import json

def get_dens(il_name):
    filename = 'dens.json'
    with open('dens.json') as fj:
        dens = json.load(fj)
    return dens[il_name.lower()]
