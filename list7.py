#list7.py

students_scores = [[1, "일길동", 100, 100, 100],[2, "이길동", 90, 90, 90,], [3, "삼길동", 80, 80, 80]]


print(students_scores[0])
print(type(students_scores[0]))

print(f'번호: {students_scores[0][0]}')
print(f'이름: {students_scores[0][1]}')
print(f'국어: {students_scores[0][2]}')
print(f'영어: {students_scores[0][3]}')
print(f'수학: {students_scores[0][4]}')
print()
print(f'번호: {students_scores[1][0]}')
print(f'이름: {students_scores[1][1]}')
print(f'국어: {students_scores[1][2]}')
print(f'영어: {students_scores[1][3]}')
print(f'수학: {students_scores[1][4]}')
print()
print(f'번호: {students_scores[2][0]}')
print(f'이름: {students_scores[2][1]}')
print(f'국어: {students_scores[2][2]}')
print(f'영어: {students_scores[2][3]}')
print(f'수학: {students_scores[2][4]}')

for i in range(len(students_scores)):
    for j in range(len(students_scores[i])):
        print(f'{students_scores[i][j]}', end ='\t')
    print()
