import mbuild as mb
from mbuild.examples import Alkane
from mbuild.lib.atoms import N4


class TetraAlkylAmmonium(mb.Compound):
    def __init__(self, chain_lengths=[2, 2, 2, 2]):
        super(TetraAlkylAmmonium, self).__init__()

        n4 = N4()
        self.add(mb.clone(n4), label='ammonium')

        for i, chain_length in enumerate(chain_lengths):
            alkyl = Alkane(n=chain_length, cap_front=False, cap_end=True)
            self.add(alkyl, label='alkyl_{}'.format(i))
            mb.force_overlap(self['alkyl_{}'.format(i)],
                self['alkyl_{}'.format(i)]['up'],
                self['ammonium']['port_{}'.format(i)])
