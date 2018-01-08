import glob
from os.path import join, split, abspath

import numpy as np


def compare_atomtypes(typed_structure, reference_structure):
    """Compare known atomtypes between structures.

    Parameters
    ----------
    typed_structure : parmed.Structure
        A parmed structure with `atom.type` attributes.
    reference_structure : parmed.Structure
        A parmed structure with `atom.type` attributes.

    Raises
    ------
    AssertionError

    """
    known_types = [atom.type for atom in reference_structure.atoms]

    generated_atom_types = list()
    for i, atom in enumerate(typed_structure.atoms):
        message = ('Found multiple or no atom types for atom {} in {}: {}\n'
                   'Should be atomtype: {}'.format(
            i, reference_structure.title, atom.type, known_types[i]))
        assert atom.type, message
        generated_atom_types.append(atom.type)

    both = zip(generated_atom_types, known_types)

    n_types = np.array(range(len(generated_atom_types)))
    known_types = np.array(known_types)
    generated_atom_types = np.array(generated_atom_types)

    non_matches = np.array([a != b for a, b in both])
    message = "Found inconsistent OPLS types in {}: {}".format(
        reference_structure.title,
        list(zip(n_types[non_matches],
                 generated_atom_types[non_matches],
                 known_types[non_matches])))
    assert not non_matches.any(), message
