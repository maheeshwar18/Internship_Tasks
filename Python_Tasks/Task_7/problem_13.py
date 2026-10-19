# Qno 13
# Sherlock and the Valid String
def isValid(s):
    freq = []
    for char in set(s):
        freq.append(s.count(char))

    for i in range(len(freq)):
        temp = freq.copy()
        temp[i] -= 1
        temp = [x for x in temp if x > 0]

        if len(set(temp)) == 1:
            return "YES"

    return "YES" if len(set(freq)) == 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
