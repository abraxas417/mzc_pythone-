#string3.py

#sequence : 인덱싱과 슬라이싱에 대한 에제입니다.

str = "Monty python"

print(str[0])

print(str[-1])

print(str[0:5])

print(str[:5])

print(str[6:])

date_weather = "20250722sunny"

#날짜(date)와 날씨(weather)을 출력하세요
date = date_weather[:8]
weather = date_weather[8:]

print(f'date: {date}')
print(f'weather : {weather}')

#날짜 데이터를 2025년 07월 22일로 변환하여 출력하세요
#2025년 07월 22일 날씨:sunny

year = date[:4]
month = date[4:6]
day = date[5:]

print(f'{year}년 {month}월 {day}일 날씨:{weather}')