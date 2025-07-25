#list13.py

menu = [['칼국수', 6000], ['비빔밥', 5500], ['돼지국밥', 7000], 
             ['돈까스', 7000], ['김밥', 2000], ['라면', 2500]]

# print(f'비빔밥 가격:{menu[1][1]} 돈가스 가격: {menu[3][1]}')

for name, price in menu:
    if name == '비빔밥' or name =='돈까스':
        print(f'{name}: {price}')

#사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가하는 코드를 작성 하시오.

a, b =input('메뉴와 가격을 추가하세요.').split()

menu.append([a, int(b)])

print(menu)


#3. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가 할 때 기존에 동일한 메뉴가 존재하는 경우 가격만 변경 되도록 코드를 작성 하시오

new_name, new_price = input("메뉴와 가격을 입력하세요. (살랑팅 10000)").split()

is_udpdated = False
for name, price in menu:
    if name == new_name:
        price = new_price
        is_udpdated = True
        print(f'{new_name} 메뉴 가격이 {new_price} 로 변경되었습니다.')
        break

if not is_udpdated:
    menu.append([new_name,new_price])