#dic11.py

menu = {
    '칼국수': 6000,
    '비빔밥': 5000,
    '돼지국밥': 7000,
    '돈까스': 7000,
    '김밥': 2000,
    '라면': 2500
}


for item, price in menu.items():
    if price < 6000:
        print(f'{item} : {price}원')