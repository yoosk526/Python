def classified_region(code):
    if (code == 0):
        exit()
    elif not (101 <= code <= 105):
        return "잘못된 입력입니다."
        
    idx = code - 100
    
    if (idx == 1):
        return "서울"
    elif (idx == 2):
        return "강릉"
    elif (idx == 3):
        return "부산"
    elif (idx == 4):
        return "광주"
    elif (idx == 5):
        return "대전"

while (1):
    code = int(input("코드를 입력하세요 (101~105): "))

    region = classified_region(code)

    print(region)
    