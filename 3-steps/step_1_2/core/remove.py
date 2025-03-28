from core.utils import *


def are_same_lists(a, b) -> bool:
    '''
    if 2 lists are same
    '''
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def find_pattern(text: list, pattern: list):
    '''
    find the pattern in a file.
    parameters:
    - text: a list of string, the file content
    - pattern: a list of string, the pattern
    '''
    res = []
    length = len(pattern)
    i = 0
    while i < len(text)-length+1:
        if are_same_lists(text[i:i+length], pattern):
            res.append([i, i+length])
            i += length
        else:
            i += 1
    return res


def get_remain_set(inset: list, indices: list):
    if len(indices) == 0:
        return [inset]
    start = inset[0]
    end = inset[1]
    res = []
    for index_tuple in sorted(indices):
        if index_tuple[0] > start:
            res.append([start, index_tuple[0]])
        start = index_tuple[1]
    if indices[-1][1] < end:
        res.append([indices[-1][1], end])
    return res


def remove_patterns(text: list, patterns: list):
    sorted_patterns = dedup_patterns(patterns)
    found_indices = []
    text_groups = [[0, len(text)]]
    for pattern in sorted_patterns:
        updated_groups = []
        for group in text_groups:
            curr_text = text[group[0]:group[1]]
            indices = find_pattern(curr_text, pattern)
            for index_tuple in indices:
                # add offset
                index_tuple[0] += group[0]
                index_tuple[1] += group[0]
            if len(indices) > 0:
                found_indices += indices
            updated_groups += get_remain_set(group, indices)
        text_groups = updated_groups

    output_text = []
    for group in text_groups:
        output_text += text[group[0]:group[1]]
    return output_text, found_indices


def init_patterns(pattern_file):
    patterns = []
    tmp = []
    for line in pattern_file:
        # TODO: make sure the spliter
        if line == EMPTYLINE or ' ' in line:
            if len(tmp) > 0:
                patterns.append(tmp)
                tmp = []
            continue
        tmp.append(line)
    return patterns


def dedup_patterns(patterns: list):
    res = []
    if len(patterns) == 0:
        return res
    sorted_patterns = sorted(patterns, key=len, reverse=False)
    strp = [''.join(p) for p in sorted_patterns]
    lenp = len(sorted_patterns)
    for i in range(lenp-1):
        found = False
        for j in range(i+1, lenp):
            if strp[i] == strp[j]:
                found = True
                break
        if not found:
            res.append(sorted_patterns[i])
    res.append(sorted_patterns[-1])
    res.reverse()
    return res


def remove_patterns_wrapper(text: list, pattern_file: list):
    patterns = init_patterns(pattern_file)
    output_text, found_indices = remove_patterns(text, patterns)
    output_text_str = '\n'.join(output_text)+'\n'
    found_indices_str = '\n'.join(
        [str([it[0]+1, it[1]]) for it in sorted(found_indices)])+'\n'
    return output_text_str, found_indices_str


def removing(filename, pattern_filename):
    text = load_file(filename)
    pattern_file = load_file(pattern_filename)
    output_text, found_indices = remove_patterns_wrapper(text, pattern_file)
    dump_file(get_filename(filename).replace('.txt', '.out.txt'), output_text)
    dump_file(get_filename(filename)+'.log', found_indices)
