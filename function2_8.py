# def menu():
#     print("1. 섭씨 온도->화씨 온도")
#     print("2. 화씨 온도->섭씨 온도")
#     print("3.종료")
#     selection = int(input("메뉴를 선택하세요: "))
#     return selection

# def ctof(c):
#     temp = c*9.0/5.0 + 32
#     return temp

# def ftoc(f):
#     temp = (f-32.0)*5.0/9.0
#     return temp

# def input_f():
#     f= float(input("화씨 온도를 입력하시오: "))
#     return f

# def input_c() :
#     c = float(input("섭씨 온도를 입력하시오: "))
#     return c

# def main() :
#     while True:
#         index = menu()
        
#         if index == 1 :
#             t = input_c()
#             t2 = ctof(t)
#             print("화씨 온도 = ", t2, "\n")
#         elif index == 2 :
#             t = input_f()
#             t2 = ftoc(t)
#             print("섭씨 온도 = ", t2, "\n")
#         else :
#             break
# main()


def menu():
    print("1.삼각형 2.사각형 3.원 4.종료")
    selection = int(input("면적을 계산할 도형을 선택하세요 : "))
    return selection


def tri(adj, opp):
    area = adj * opp 
    return area

def lec(g,s):
    area = g * s 
    return area

def circle(r):
    area = 3.14 * r**2
    return area

def input_tri():
    adj = int(input('밑변: '))
    opp = int(input('높이: '))
    return [adj, opp]

def input_lec():
    g = int(input("가로: "))
    s = int(input("세로: "))
    return [g,s]    

def input_circle():
    r = int(input("반지름의 길이: "))
    return r

def main():
    
    while True:
        index=menu()
        if index ==1:
            a,b = input_tri()
            t =tri(a,b)
            print(t)
        elif index ==2:
            a,b = input_lec()
            t =lec(a,b)
            print(t)
            
        elif index ==3:
            a = input_circle()
            t =circle(a)
            print(t)
        else:
            break

main()