import os
from pkg_resources import resource_filename

from foyer import Forcefield
import mbuild as mb

def get_fn(file_name):
    """Get the path to a file in /lib/."""
    full_name = resource_filename('ilforcefields', os.path.join('lib', file_name))
    return full_name


def get_ff_path(ff_name):
    """Get the path to a force field xml file """
    """in a directory of the same name."""
    ff_path = resource_filename('ilforcefields',
                                os.path.join(ff_name, ff_name + '.xml'))
    return ff_path


def get_ff(ff_name):
    """Get the Forcefield object from a force field xml file """
    """in a directory of the same name."""
    ff_path = get_ff_path(ff_name)
    FF = Forcefield(ff_path)
    return FF

def get_il(il_name):
    cache_dir = resource_filename('ilforcefields', 'lib/un-typed')
    filename = '{}.mol2'.format(il_name)
    if any(file == filename for file in os.listdir(cache_dir)):
        mb.Compound.__init__(self)

        il = mb.load(os.path.join(cache_dir, filename), compound=self)
        il.name = il_name
    return il
