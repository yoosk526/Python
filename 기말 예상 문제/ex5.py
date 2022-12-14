
# num1 = input("정수 입력 : ")
# if ('.' in num1):
#     print("정수를 입력하세요.")
#     exit()
# else:
#     num1 = int(num1)

# num2 = input("정수 입력 : ")
# if ('.' in num2):
#     print("정수를 입력하세요.")
#     exit()
# else:
#     num2 = int(num2)
#menu = int(input("연산 종류(1:덧셈 2:뺄셈 3:곱셈 4:나눗셈) : "))



def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    num1 = int(input("정수 입력 : "))
    num2 = int(input("정수 입력 : "))
    menu = int(input("연산 종류(1:덧셈 2:뺄셈 3:곱셈: 4:나눗셈) : "))
except:
    print("정수를 입력하세요.")
else:
    if not (1 <= menu <= 4):
        print("잘못된 연산자입니다.")
        exit()
    elif (menu == 1):
        result = add(num1, num2)
    elif (menu == 2):
        result = sub(num1, num2)
    elif (menu == 3):
        result = mul(num1, num2)
    elif (menu == 4):
        result = div(num1, num2)
    
    print("계산 결과 = ", result)

