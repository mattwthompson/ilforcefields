import inspect
import os

import mbuild as mb
from pkg_resources import resource_filename

class GetIL(mb.Compound):
    def __init__(self, il_name):
        cache_dir = resource_filename('ilforcefields', 'lib/un-typed')
        filename = '{}.mol2'.format(il_name)
        if any(file == filename for file in os.listdir(cache_dir)):
            mb.Compound.__init__(self)

            mb.load(os.path.join(cache_dir, filename), compound=self)
            self.name = il_name
