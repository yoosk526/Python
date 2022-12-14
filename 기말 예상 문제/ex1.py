# reg_list = []       # 이름 등록 
# fin_list = []       # 완주자 기록
# not_fin_list = []   # 미완주자 기록

# num_people = int(input("참가자 수: "))

# while (num_people > 0):
#     name = input("이름 입력: ")

#     if (name not in reg_list):      
#         reg_list.append(name)
#         num_people -= 1

#     elif (name in reg_list):
#         reg_list.remove(name)
#         fin_list.append(name)

# if (len(reg_list) != 0):
#     not_fin_list = reg_list
    
# #print(reg_list)
# #print(fin_list)
# print("완주하지 못한 참가자:", not_fin_list[0])

num = int(input("참가자 수 : "))
people = set()

for i in range(2 * num - 1):
    name = input("이름 입력 : ")

    if name not in people:
        people.add(name)
    else:
        people.remove(name)

print("완주하지 못한 참가자 : ", people.pop())
