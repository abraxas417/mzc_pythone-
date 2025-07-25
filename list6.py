#list6.py

colors = ['red', 'green', 'blue', 'white', 'black']


#colors 리스트 정보를 조회하여 출력하시오
#인덱스, 요소(항목)
#0. 'red'
#1. 'green'
#2  'blue'
# ....


for i in range(len(colors)):
    print(f'colors[{i}] : {colors[i]}')


# 'blue'-> 'yellow' 변경
colors[2] ='yellow'

print(colors)