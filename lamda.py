# lamda.py

# 람다 함수에 대한 예제 프로그램입니다.

# def say_hello(user_name):
#     print(f'Hello, {user_name}')


hello = lambda user_name: 'Hello, ' + user_name

print(type(hello))

print(hello ('ojs'))