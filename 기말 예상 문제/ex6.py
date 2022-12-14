num_str = input("양의 정수를 입력하시오: ")

num = int(num_str)

for i in range(len(num_str), 0, -1):      # i : 3, 2, 1 식으로 내려감
    iter = num // 10**(i - 1)
    print("* "*iter)                # 253 / 10^2, 53 / 10^1, 3 / 10^0
    num = num % (10**(i - 1))       # 253 -> 53, 53 -> 3, 3 -> 0
    print("\n")

