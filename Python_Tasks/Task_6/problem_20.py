# Qno 20
# Validating Phone numbers
import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        number = input()

        if re.match(r'^[789][0-9]{9}$', number):
            print("YES")
        else:
            print("NO")
