applyList = [
    ("홍길동", 95, 80),
    ("이순신", 60, 75),
    ("강감찬", 75, 70),
    ("최불암", 85, 85),
    ("이연경", 90, 90)    
]

pass_num = 0
fail_num = 0

temp_avg = 0.0
avg_rec = []        # 5명의 평균 값을 저장할 list
result = []         # 5명의 Pass/Fail을 저장할 list

for i in range(len(applyList)):
    temp_avg = (applyList[i][1] + applyList[i][2]) / 2
    avg_rec.append(temp_avg)
    if (temp_avg >= 80):
        result.append('PASS')
        pass_num += 1
    else:
        result.append('FAIL')
        fail_num += 1


print("\t**입사 성적 발표**")
print("이  름\t\t점  수\t\t결과")

for i in range(len(applyList)):
    print("{}\t\t{:5.2f}\t\t{}".format(applyList[i][0], avg_rec[i], result[i]) )   # print(applyList[i][0], "\t\t", "%.2f\t\t"%(avg_rec[i]), result[i])

print("="*37)

print("합격자 %6d명"%pass_num)
print("불합격 %6d명"%fail_num)
print("응시자 전체 %d명"%(len(applyList)))


