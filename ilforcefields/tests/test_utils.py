from ilforcefields.utils import get_ff, get_il


IMPLEMENTED_FORCE_FIELDS = ['lopes', 'kpl', 'ngkpl']
IMPLEMENTED_ILS = ['emim', 'bmim', 'hmim', 'omim', 'otf', 'tf2n', 'bf4', 'pf6', 'dca']


def test_get_ff():
    for ff in IMPLEMENTED_FORCE_FIELDS:
        FF = get_ff(ff)


def test_get_il():
    for il in IMPLEMENTED_ILS:
        get_il(il)
