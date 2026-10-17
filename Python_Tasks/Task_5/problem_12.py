# Qno 12
# Capitalize
import math
import os
import random
import re
import sys

def solve(s):
    result = ""
    new_word = True

    for char in s:
        if char == " ":
            result += char
            new_word = True
        elif new_word:
            result += char.upper()
            new_word = False
        else:
            result += char

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
