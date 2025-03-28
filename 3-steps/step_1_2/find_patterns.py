import argparse
from core.find import LCS_in_dir
from core.utils import dump_file


def main():
    parser = argparse.ArgumentParser(
        description='Find the longest common line sequence in a directory of text files.')
    parser.add_argument(
        'directory', help='Path to the directory containing text files')
    parser.add_argument('-p', '--pattern', action='store_true',
                        help='Find the common patterns.')
    parser.add_argument('-o', '--order', action='store_true',
                        help='Keep the monotonically increasing order.')
    parser.add_argument(
        '-f', '--file', help='Path to the target file to keep order. Use the first file if not specified.')
    parser.add_argument(
        '-d', '--dump', action='store_true', help='Dump the results.')

    args = parser.parse_args()
    directory_path = args.directory
    # pattern = True if args.pattern else False
    pattern = False if args.pattern else True
    order = True if args.order else False
    dump = False if args.dump else True
    filepath = args.file if args.file else None

    patterns = LCS_in_dir(
        directory_path, pattern, order, filepath)

    if len(patterns) == 0:
        print("No common lines found.")
    else:
        if dump:
            dump_file('patterns', patterns+'\n')
        else:
            print(patterns)


if __name__ == "__main__":
    main()
