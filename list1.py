#list1.py
#리스트에 대한 에제 프로그램입니다.
#list : collaction, sequence 자료형

subject_list = ['영어', '수학', '사회', '과학']

print(subject_list)
print(f'subject_list 자료형 : {type(subject_list)}')

print(subject_list[0])

print({type(subject_list[3])})

print(f'subject_list 항목의 개수: {len(subject_list)}')

for subject in subject_list:
    print(subject)
    