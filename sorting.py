student_tuples = [
        ['john', 'A', 15],
        ['jane', 'B', 12],
        ['dave', 'B', 10],
]

print sorted(student_tuples, key=lambda student: student[2])


heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]

for i in range(len(heuristic)):
    print sorted(heuristic, key=lambda last: last[5])[i]