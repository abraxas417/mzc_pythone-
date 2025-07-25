#dic2.py

member = {
    'user_name' : '일길동' ,
    'age': 10,
    'email' : 'python@gmaol.com'

}

#이름과 나이, 이메일 정보를 출력하세요.
print(f'user_name: {member['user_name']}')
print(f'age: {member['age']}')
print(f'email: {member['email']}')
#이름을 '홍길동으로 변경하시오.

member['user_name'] = '홍길동'

print(member)