#dic5.py


member_list = [
    {'user_name' : '일길동' ,
    'age': 10,
    'email' : 'python@gmaol.com'
    },


 {
    'user_name' : '이길동' ,
    'age': 20,
    'email' : 'python1@gmaol.com'

},



{
    'user_name' : '삼길동' ,
    'age': 30,
    'email' : 'python2@gmaol.com'

}

]

for member in member_list:
    print(type(member))
    user_name =member['user_name']
    age = member['age']
    email = member['email']
    print(f'{user_name}, {age}, {email}')