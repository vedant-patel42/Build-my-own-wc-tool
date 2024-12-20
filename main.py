#!/usr/bin/env python3

import sys
import argparse
import os

def countBytes(file):
    try:
        bytes_count = os.path.getsize(file)
        return bytes_count
    except Exception as e:
        return e

def countLines(file):
    try:
        with open(file, 'r') as f:
            return len(f.readlines())
    except Exception as e:
        return e

def countWords(file):
    try:
        with open(file,'r') as f:
            words = [word for line in f for word in line.strip().split()]
            return len(words)
    except Exception as e:
        return e

def process_file(file, count_bytes_flag):
    byte_count = 0

    for line in file:
        if count_bytes_flag:
            byte_count += len(line.encode('utf-8'))

    return byte_count

def main():
    cmd = sys.argv

    if cmd[1] == 'ccwc':
        file_name = cmd[-1]
        if cmd[2] == '-c':
            count_bytes = countBytes(file_name)
            print(count_bytes, file_name)
        elif cmd[2] == '-l':
            count_lines = countLines(file_name)
            print(count_lines, file_name)
        elif cmd[2] == '-w':
            count_words = countWords(file_name)
            print(count_words, file_name)
        else:
            count_bytes = countBytes(file_name)
            count_lines = countLines(file_name)
            count_words = countWords(file_name)
            print(count_words, count_lines, count_bytes, file_name)

if __name__ == "__main__":
    main()