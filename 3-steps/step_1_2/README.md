# Finding Common Patterns

## Usage

### Find patterns

```sh
python3 find_patterns.py <path_to_txt_files> [-f <path_to_target_file>] [-o] [-p] [-d]
```

Arguments:
- `<path_to_txt_files>`: the path to a directory storing the `.txt` files.
- `-f`: to indicate a target file, the common patterns will be found based on the order of this file, default value is the first file in `<path_to_txt_files>`.
- `-o`: to enable the ordered mode, the common patterns will be found in order, this flag is `False` if not specified.
- `-p`: to disable the pattern grouping mode, this flag is `True` if not specified.
- `-d`: to disable dumping the results, if specified, the results will not be dumped, but printed.

### Remove patterns

```sh
python3 remove_patterns.py <path_to_txt_files> <path_to_pattern_file>
```

Remove the patterns in `<path_to_pattern_file>` from `.txt` files in `<path_to_txt_files>`.

### Find and Remove patterns

```sh
python3 find_remove_patterns.py <path_to_txt_files> [-f <path_to_target_file>] [-o] [-p]
```

Arguments are the same as **Find patterns** (removing the `-d` flag). 

The results will be stored in 3 folders:
- `step1.1-hbw_vgr_common`
- `step1.2-noises_removed`
- `step2-extracted_common_part_retrieval`
