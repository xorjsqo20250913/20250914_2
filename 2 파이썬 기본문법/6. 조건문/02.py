score = 85
if score >= 90 :
    print("90점 이상입니다")

print('if와 상관 없는 문장')

list_1 = [1,2,3,4,5]
if 2 in list_1 :
    print("2가 list_1에 있습니다")
dict_1 = {'name':'홍길동', 'age':20}
if 'name' in dict_1 :
    print("name이 dict_1에 있습니다")

# 중첩 조건문
# if조건문 1:
#  if 조건문2:
#    실행문
#  else:
#    실행문
#  else:
#   실행문
# 예시
num = 15    
if num >= 10 :
    if num % 3 == 0 :
        print("10이상의 짝수입니다")
    else :
        print("10이상의 홀수입니다")

if num % 2 == 0 and num % 3 == 0:
    print("2와3의 공배수입니다")
