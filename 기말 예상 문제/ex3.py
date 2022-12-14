
# word = text.split()

# word_dict = {}      

# for i in range(len(word)):
#     if (word[i] not in word_dict.keys()):
#         word_dict[word[i]] = 1              
    
#     elif (word[i] in word_dict.keys()):    
#         word_dict[word[i]] += 1

# print("총장님 인사말의 총 단어수: {}".format(len(word)))
# print(f"총장님의 인사말 중 캠퍼스 단어의 반복 횟수 : {word_dict['캠퍼스']}")

text = '''여러분 안녕하세요. 여러분을 캠퍼스 에서 뵙게 되어 반갑습니다.
캠퍼스 엔 가을의 짙은 향기와 바람이 가득합니다. 캠퍼스 의 이곳 저곳이 노랗고
울긋불긋한 단풍으로 화려한 그림을 그리고 있네요. 캠퍼스 안에서 여러분의
꿈이 조금씩 실현되어지길 기대합니다. 감사합니다.'''

word = text.split()

word_dict = {}      # 딕셔너리 형태로 데이터 분류함 (단어 : 개수)

for i in range(len(word)):
    if word[i] not in word_dict.keys():      # 처음 만난 단어를 등록, 개수 = 1로 초기화
        word_dict[word[i]] = 1
    else:                                    # 이미 있는 단어라면
        word_dict[word[i]] += 1

print("총장님 인사말의 총 단어수 : ", len(word))
print("총장님의 인사말 중 캠퍼스 단어의 반복 횟수 : {}".format(word_dict['캠퍼스']))