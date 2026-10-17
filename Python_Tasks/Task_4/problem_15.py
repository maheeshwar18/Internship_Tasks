# Qno 15
# Word Order
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    words = OrderedDict()

    for i in range(n):
        word = input()

        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print(len(words))
    print(*words.values())
