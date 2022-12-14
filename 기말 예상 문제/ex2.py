def name_coffee(name, coffee):
    print("{} 고객님, 주문하신 {} 나왔습니다.".format(name, coffee))

num = 1

while (1):
    coffee = input("커피 종류를 입력하세요: ")

    if (coffee == '마감'):
        break

    else:
        name = input("고객명을 입력하세요: ")
        if (len(name) == 0):
            name_coffee(num, coffee)
        else:
            name_coffee(name, coffee)

    num += 1