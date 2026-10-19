# Qno 17
# Separate the Numbers
def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        value = first
        result = ""

        while len(result) < len(s):
            result += str(value)
            value += 1

        if result == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
