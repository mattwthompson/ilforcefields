import pathlib
from pkg_resources import resource_filename


def get_root_path():
    import ilforcefields
    return pathlib.Path(ilforcefields.__file__).parent


def get_forcefield_path():
    for dir_path in get_ff_path():
        file_pattern = os.path.join(dir_path, '*/*.xml')
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
    return file_paths


def get_forcefield(name='lopes'):
    name = '/' + name.lower()
    from foyer import Forcefield
    path = pathlib.Path(str(get_root_path()) + name + name + '.xml')
    return Forcefield(path)


def load_LOPES():
    return get_forcefield(name='lopes')


def load_KPL():
    return get_forcefield(name='kpl')


def load_NGKPL():
    return get_forcefield(name='ngkpl')
