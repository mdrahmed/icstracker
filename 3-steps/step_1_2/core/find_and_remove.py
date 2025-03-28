from core.find import *
from core.remove import remove_patterns_wrapper

FOLDERS = ['step1.1-hbw_vgr_common',
           'step1.2-noises_removed',
           'step2-extracted_common_part_retrieval']


def init_dir():
    FOLDERS.append(os.path.join(FOLDERS[1], 'logs'))
    for dir in FOLDERS:
        if not os.path.exists(dir):
            os.mkdir(dir)


def find_and_remove_patterns(directory: str, pattern: bool = False, order: bool = False, filepath: str = None) -> str:
    txt_files = get_file_list(directory)
    file_dict = {}
    for file in txt_files:
        file_path = os.path.join(directory, file)
        file_dict[file] = load_file(file_path)

    txt_files = sorted(txt_files, reverse=False)
    common_sequence = None
    if filepath:
        if os.path.isfile(filepath):
            common_sequence = load_file(filepath)
            key = get_filename(filepath)
            if key in txt_files:
                txt_files.remove(key)
        else:
            print('Error: File "{}" is not found.'.format(filepath))
            exit(1)
    else:
        key = txt_files[0]
        common_sequence = file_dict[key]
        txt_files.remove(key)
    for file in txt_files:
        text = file_dict[file]
        tmp = None
        if order:
            tmp = find_longest_common_subsequences_ordered(
                common_sequence, text)
        else:
            tmp = find_longest_common_subsequences(
                common_sequence, text)
        res = pattern2list(tmp, pattern)
        output_text, found_indices = remove_patterns_wrapper(text, res)
        pattern_str = result_handler(res, pattern)+'\n'
        dump_file(os.path.join(FOLDERS[0], file+'.pattern'), pattern_str)
        dump_file(os.path.join(FOLDERS[1], file.replace(
            '.txt', '.out.txt')), output_text)
        dump_file(os.path.join(FOLDERS[-1], file+'.log'), found_indices)
