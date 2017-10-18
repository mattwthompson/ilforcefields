from pkg_resources import resource_filename

from foyer import Forcefield

def get_lopes():
    LOPES = Forcefield(resource_filename('ilforcefields',
                                         'lopes/lopes.xml'))
    return LOPES
