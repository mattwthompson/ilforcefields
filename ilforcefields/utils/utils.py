import os
from pkg_resources import resource_filename

def get_fn(file_name):
    """Get the path to a file in /lib/."""
    full_name = resource_filename('ilforcefields', os.path.join('lib', file_name))
    return full_name

def get_forcefield(ff_name):
    """Get the path to a force field xml file in a directory of the same name."""
    full_name = resource_filename('ilforcefields',
                                  os.path.join(ff_name, ff_name + '.xml'))
    return full_name
