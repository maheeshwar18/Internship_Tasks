# Qno 7
# Alphabet Rangoli
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3

    for i in range(size):
        s = "-".join(alphabet[size-1:size-i-1:-1] + alphabet[size-i-1:size])
        print(s.center(width, "-"))

    for i in range(size-2, -1, -1):
        s = "-".join(alphabet[size-1:size-i-1:-1] + alphabet[size-i-1:size])
        print(s.center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
