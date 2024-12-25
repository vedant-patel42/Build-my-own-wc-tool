#!/usr/bin/env python3

import sys
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

def countChars(file):
    try:
        with open(file, 'rb') as f:
            content = f.read()
            content = content.decode('utf-8')
            return len(content)
    except Exception as e:
        return e

def main():
    cmd = sys.argv
    c = cmd[0].split('/')

    if c[-1] == 'ccwc':
        file_name = cmd[-1]
        if cmd[1] == '-c':
            count_bytes = countBytes(file_name)
            print(count_bytes, file_name)
        elif cmd[1] == '-l':
            count_lines = countLines(file_name)
            print(count_lines, file_name)
        elif cmd[1] == '-w':
            count_words = countWords(file_name)
            print(count_words, file_name)
        elif cmd[1] == '-m':
            count_char = countChars(file_name)
            print(count_char, file_name)
        else:
            count_bytes = countBytes(file_name)
            count_lines = countLines(file_name)
            count_words = countWords(file_name)
            print(count_words, count_lines, count_bytes, file_name)

if __name__ == "__main__":
    main()