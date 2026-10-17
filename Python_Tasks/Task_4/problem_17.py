# Qno 17
# Finding the Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for i in range(n):
        name, *marks = input().split()
        student_marks[name] = list(map(float, marks))

    query_name = input()

    average = sum(student_marks[query_name]) / len(student_marks[query_name])

    print(f"{average:.2f}")
