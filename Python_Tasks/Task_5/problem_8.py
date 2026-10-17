# Qno 8
# Set.add()
if __name__ == '__main__':
    n = int(input())
    countries = set()

    for i in range(n):
        country = input()
        countries.add(country)

    print(len(countries))
