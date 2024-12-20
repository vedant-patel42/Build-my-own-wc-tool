#!/usr/bin/env python3

import sys
import argparse
import os

def count_bytes(file):
    return sum(len(line.encode('utf-8')) for line in file)

def process_file(file, count_bytes_flag):
    byte_count = 0

    for line in file:
        if count_bytes_flag:
            byte_count += len(line.encode('utf-8'))

    return byte_count

def main():
    cmd = sys.argv
    # parser = argparse.ArgumentParser(description="Custom wc command implementation.")
    # parser.add_argument("files", nargs="+", help="Files to process.")
    # parser.add_argument("-c", action="store_true", help="Count bytes.")

    args = parser.parse_args()

    if cmd[0] == 'ccwc':
        file_name = cmd[-1]
        try:
            bytes_count = os.path.getsize(file_name)
        except Exception as e:
            print(f"Error processing file {file_name}: {e}", file=sys.stderr)

    # if not args.c:
    #     print("Error: Please provide the -c option to count bytes.", file=sys.stderr)
    #     sys.exit(1)
    # for file_name in args.files:
    #     try:
    #         print(os.path.getsize(file_name))
    #         with open(file_name, "r", encoding="utf-8") as file:
    #             byte_count = process_file(file, args.c)
    #             print(f"{byte_count:>8} {file_name}")
    #     except Exception as e:
    #         print(f"Error processing file {file_name}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()