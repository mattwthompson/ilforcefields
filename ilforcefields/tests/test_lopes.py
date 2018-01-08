import glob
import itertools as it
import os
from pkg_resources import resource_filename

import parmed as pmd
import pytest
from foyer import Forcefield
import numpy as np

from ilforcefields.utils.utils import get_ff
from ilforcefields.tests.utils import compare_atomtypes


def test_get_lopes():
    from ilforcefields.utils.utils import get_ff
    LOPES = get_ff('lopes')


LOPES = Forcefield(resource_filename('ilforcefields', os.path.join('lopes', 'lopes.xml')))

LOPES_TESTFILES_DIR = resource_filename('ilforcefields', 'lopes_validation')


class TestLOPES(object):

    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()

    top_files = glob.glob(os.path.join(LOPES_TESTFILES_DIR, '*/*.top'))
    mol2_files = glob.glob(os.path.join(LOPES_TESTFILES_DIR, '*/*.mol2'))

    implemented_tests_path = os.path.join(os.path.dirname(__file__),
                                          'implemented_tests.txt')
    with open(implemented_tests_path) as f:
        correctly_implemented = [line.strip() for line in f]

    def find_correctly_implemented(self):
        with open(self.implemented_tests_path, 'a') as fh:
            for mol_path in it.chain(self.top_files, self.mol2_files):
                _, mol_file = os.path.split(mol_path)
                mol_name, ext = os.path.splitext(mol_file)
                try:
                    self.test_atomtyping(mol_name)
                except Exception as e:
                    print(e)
                    continue
                else:
                    if mol_name not in self.correctly_implemented:
                        fh.write('{}\n'.format(mol_name))

    @pytest.mark.parametrize('mol_name', correctly_implemented)
    def test_atomtyping(self, mol_name, testfiles_dir=LOPES_TESTFILES_DIR):
        files = glob.glob(os.path.join(testfiles_dir, mol_name, '*'))
        for mol_file in files:
            _, ext = os.path.splitext(mol_file)
            if ext == '.top':
                top_filename = '{}.top'.format(mol_name)
                gro_filename = '{}.gro'.format(mol_name)
                top_path = os.path.join(testfiles_dir, mol_name, top_filename)
                gro_path = os.path.join(testfiles_dir, mol_name, gro_filename)
                structure = pmd.load_file(gro_path)
                reference_structure = pmd.load_file(top_path, xyz=gro_path, parametrize=False)
        typed_structure = LOPES.apply(structure)

        compare_atomtypes(typed_structure, reference_structure)

        assert np.round(np.sum([a.charge for a in typed_structure.atoms]), 6) % 1.0 == 0.0

if __name__ == '__main__':
    TestLOPES().find_correctly_implemented()
