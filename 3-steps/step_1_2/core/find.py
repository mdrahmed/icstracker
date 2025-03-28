from difflib import SequenceMatcher
from core.utils import *


def find_longest_common_subsequences(list_a: list, list_b: list) -> list:
    res = []
    len_a, len_b = len(list_a), len(list_b)
    left_a = 0
    while left_a < len_a:
        max_a = -1
        left_b = 0
        while left_b < len_b:
            curr_a = left_a
            curr_b = left_b
            while list_a[curr_a] == list_b[curr_b]:
                if curr_a - left_a > max_a:
                    max_a = curr_a - left_a
                curr_a += 1
                curr_b += 1
                if curr_a >= len_a or curr_b >= len_b:
                    break
            if curr_a >= len_a or curr_b >= len_b:
                break
            left_b = curr_b+1
        if max_a > -1:  # found
            res.append(list_a[left_a:left_a+max_a+1])
            left_a += max_a+1
        else:  # not found
            left_a += 1
    return res


def find_longest_common_subsequences_ordered(list_a: list, list_b: list) -> list:
    matcher = SequenceMatcher(None, list_a, list_b)
    matching_blocks = matcher.get_matching_blocks()
    res = []
    for i, j, size in matching_blocks:
        if size > 0:
            res.append(list_a[i:i + size])
    return res


def LCS_in_dir(directory: str, pattern: bool = True, order: bool = True, filepath: str = None) -> str:
    txt_files = get_file_list(directory)
    file_paths = []
    for file in txt_files:
        file_paths.append(os.path.join(directory, file))
    return LCS_in_filepaths(file_paths, pattern, order, filepath)


def LCS_in_filepaths(file_paths: list, pattern: bool = True, order: bool = True, filepath: str = None) -> str:
    txt_files = file_paths
    txt_files = sorted(txt_files, reverse=False)
    target_file = None
    if filepath:
        if os.path.isfile(filepath):
            target_file = load_file(filepath)
            key = get_filename(filepath)
            for file in txt_files:
                if key == get_filename(file):
                    txt_files.remove(file)
                    break
        else:
            print('Error: File "{}" is not found.'.format(filepath))
            exit(1)
    else:
        key = txt_files[0]
        target_file = load_file(key)
        txt_files.remove(key)
    file_list = []
    for file in txt_files:
        file_list.append(load_file(file))

    common_sequence = LCS_in_list(file_list, target_file, pattern, order)

    return result_handler(common_sequence, pattern)


def LCS_in_list(file_list: list, target_file: list, pattern: bool = True, order: bool = True):
    common_sequence = target_file
    for file in file_list:
        tmp = None
        if order:
            tmp = find_longest_common_subsequences_ordered(
                common_sequence, file)
        else:
            tmp = find_longest_common_subsequences(
                common_sequence, file)
        res = pattern2list(tmp, pattern)
        common_sequence = res
    return common_sequence


def pattern2list(patterns: list, pattern_title: bool):
    res = []
    for block in patterns:
        for line in block:
            res.append(line)
        if pattern_title:
            # add the pattern spliter
            res.append(EMPTYLINE)
    return res


def result_handler(result: list, pattern: bool) -> str:
    def result_printer(result: list) -> str:
        return_strings = []
        for index, block in enumerate(result):
            tmp = []
            tmp.append('Pattern {}'.format(index+1))
            for line in block:
                tmp.append(line)
            return_strings.append('\n'.join(tmp)+'\n')
        return_strings.append("Number of patterns: {}".format(len(result)))
        return '\n'.join(return_strings)

    if pattern:
        tmp, res = [], []
        for line in result:
            if line == EMPTYLINE:
                # a new pattern
                if len(tmp) > 0:
                    res.append(tmp)
                tmp = []
            else:
                tmp.append(line.strip())
        return result_printer(res)
    else:
        return '\n'.join([line.strip() for line in result])
