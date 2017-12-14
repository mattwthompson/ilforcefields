from pkg_resources import resource_filename
import warnings

from foyer import Forcefield


def get_lopes():
    warnings.warn("This is deprecated, instead use "
                  "ilforcefield.utils.utils.get_ff('lopes')",
                  DeprecationWarning)

    LOPES = Forcefield(resource_filename('ilforcefields',
                                         'lopes/lopes.xml'))
    return LOPES
