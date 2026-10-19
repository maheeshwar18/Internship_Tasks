# Qno 15
# Game of Thrones - I
def gameOfThrones(s):
    odd = 0
    for char in set(s):
        if s.count(char) % 2 != 0:
            odd += 1
    if odd <= 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
