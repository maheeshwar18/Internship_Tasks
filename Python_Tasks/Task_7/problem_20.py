# Qno 20
# Super Reduced String
def superReducedString(s):
    result = []

    for char in s:
        if result and result[-1] == char:
            result.pop()
        else:
            result.append(char)

    if result:
        return "".join(result)

    return "Empty String"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
