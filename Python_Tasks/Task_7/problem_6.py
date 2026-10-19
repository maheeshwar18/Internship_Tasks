# Qno 6
# Pangrams
def pangrams(s):
    s = s.lower()
    letters = set(s)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in letters:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')
