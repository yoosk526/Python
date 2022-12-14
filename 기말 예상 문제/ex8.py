shape_list = ['삼각형', '사각형', '원']

def Area(shape):
    if (shape == shape_list[0]):
        w = int(input("밑변 입력 : "))
        h = int(input("높이 입력 : "))
        area = w * h / 2
    elif (shape == shape_list[1]):
        w = int(input("밑변 입력 : "))
        h = int(input("높이 입력 : "))
        area = w * h
    elif (shape == shape_list[2]):
        r = int(input("반지름 입력 : "))
        area = 3.14 * r * r

    return area


while (1):
    shape = input("넓이를 구할 도형입력(삼각형/사각형/원): ")

    if (len(shape) == 0):
        print("프로그램 종료")
        break
    
    if (shape not in shape_list):
        print("오류: 잘못 입력하셨습니다!")
    else:
        area = Area(shape)
        print("%s의 넓이는 %.1f입니다."%(shape, area))