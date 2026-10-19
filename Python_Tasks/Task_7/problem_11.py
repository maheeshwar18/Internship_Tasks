# Qno 11
# Two Strings
def twoStrings(s1, s2):
    for char in set(s1):
        if char in s2:
            return "YES"

    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
