import os
from pkg_resources import resource_filename

from foyer import Forcefield


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
