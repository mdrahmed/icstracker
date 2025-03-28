import os


EMPTYLINE = ''
PREFIX = 'FFF Function: '
IGNORE = [PREFIX]


def load_file(filename: str, ignore: bool = True) -> list:
    res = []
    with open(filename) as rd:
        for line in rd:
            # remove the 'FFF Function: '
            # func_name = line.strip().split()[-1]
            func_name = line
            if ignore:
                for ig in IGNORE:
                    func_name = func_name.replace(ig, '')
            func_name = func_name.strip()
            if len(func_name) > 0:
                res.append(func_name)
    return res


def dump_file(filename: str, data: str):
    with open(filename, 'w', encoding='utf-8') as wt:
        wt.write(data)


def get_file_list(directory: str, txt: bool = True) -> list:
    res = []
    for f in os.listdir(directory):
        if (txt and f.endswith('.txt')) or (not txt):
            res.append(f)
    return res


def get_filename(filepath: str):
    return filepath.split(
        os.path.sep)[-1].split('/')[-1].split('\\')[-1]
