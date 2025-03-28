import argparse
from core.remove import removing

def main():
    parser = argparse.ArgumentParser(
        description='Remove the patterns from a text file.')
    parser.add_argument(
        'file', help='Path to the text file')
    parser.add_argument(
        'patterns', help='Path to the pattern file')

    args = parser.parse_args()
    file_path = args.file
    pattern_path = args.patterns

    removing(file_path, pattern_path)


if __name__ == "__main__":
    main()
