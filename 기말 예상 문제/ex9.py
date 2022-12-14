mlist = ['뜨아', '아아', '라떼', '모카']
plist = [2000, 3000, 3500, 4000]

print("** 자판기 판매 메뉴 **")
for i in range(len(mlist)):
    print("{} : {} {}".format(i + 1, mlist[i], plist[i]))

money = int(input("\n돈을 투입하세요 : "))

while (1): 
    menu = int(input("\n메뉴 선택 (종료:0) :"))
    if (menu == 0):
        print("자판기 종료, 잔액 %d 반환"%money)
        break
    elif (money - plist[menu - 1] < 0):
        print("잔액부족")
    else:
        print("%s 구입완료"%mlist[menu - 1])
        money = money - plist[menu - 1]
    
    print(f"잔액 : {money}")