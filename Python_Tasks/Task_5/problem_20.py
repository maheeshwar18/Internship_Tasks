# Qno 20
# Piling Up!
from collections import deque

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        blocks = deque(map(int, input().split()))

        top = float('inf')

        while blocks:
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop()

            if current > top:
                print("No")
                break

            top = current
        else:
            print("Yes")
