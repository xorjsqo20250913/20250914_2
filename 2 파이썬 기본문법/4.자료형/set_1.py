# SET의 기본 사용법
# SET은 중복을 허용하지 않고 순서가 없으며, 변경이 불가능한 자료형이다
# - 순서를 보장하지 않는다
# - 집합연산 가능(교집합, 합집합, 차집합)
# - 서로 다른 자료형끼리 전환이 가능하다 ( 리스트 <--> 튜플)

# 1. set 생성 방법
print("1. set 생성 예제")
set1 = {1, 2, 3, 4, 5}  # 중괄호를 사용하여 생성
set2 = set([1, 2, 2, 3, 3, 4])  # set() 함수를 사용하여 생성 (중복 값은 자동 제거)
print("set1:", set1)
print("set2:", set2)  # 중복된 2, 3이 제거됨
print()

# 2. 집합 연산 예제
print("2. 집합 연산 예제")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("A:", A)
print("B:", B)
print("교집합 (A & B):", A & B)  # intersection
print("합집합 (A | B):", A | B)  # union
print("차집합 (A - B):", A - B)  # difference
print()

# 3. 자료형 변환 예제
print("3. 자료형 변환 예제")
my_list = [1, 2, 2, 3, 3, 3]
my_tuple = (4, 5, 5, 6, 6, 6)

# 리스트를 set으로 변환 (중복 제거)
set_from_list = set(my_list)
print("원본 리스트:", my_list)
print("리스트에서 변환된 set:", set_from_list)

# 튜플을 set으로 변환 (중복 제거)
set_from_tuple = set(my_tuple)
print("원본 튜플:", my_tuple)
print("튜플에서 변환된 set:", set_from_tuple)

# set을 리스트로 변환
list_from_set = list(set_from_tuple)
print("set에서 변환된 리스트:", list_from_set)