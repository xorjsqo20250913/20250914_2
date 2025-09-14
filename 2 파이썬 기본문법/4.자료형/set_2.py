#  리스트연산자
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print("list_1 + list_2 =", list_1 + list_2)  # 리스트 연결

list_1.append(list_2)
print('list_1 =',list_1)
list_1.extend(list_2)
print('list_1 =',list_1)
print("list_1 * 3 =", list_1 * 3)  # 리스트 반복

# 문자열
str_1 = "Hello"
str_2 = "World"
print("str_1 + str_2 =", str_1 + str_2)  # 문자열 연결
print("str_1 * 3 =", str_1 * 3)  # 문자열 반복

# set의 기본 사용법
# 중복허용 안함
set_1 = {1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8}
print("set_1 =", set_1)

# set에서 특정 위치에 단일 값에 접근하려면
# SET을 사용하는 이유? 중복된 값을 제거하고, 집합연산을 하기 위해서
# 보통 list를 쓰다가 두 집합사이에 공통된걸 찾고싶으면 set으로 바꿔서 교집합을 찾음

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
print('set_1 & set_2 =', set_1 & set_2) # 교집합
print('set_1.intersection(set_2) =', set_1.intersection(set_2)) # 교집합
# 29,30 셀 같음
# 합집합
print('set_1 | set_2 =', set_1 | set_2) # 합집합
print('set_1.union(set_2) =', set_1.union(set_2)) # 합집합
# 차집합
print('set_1 - set_2 =', set_1 - set_2) # 차집합
print('set_1.difference(set_2) =', set_1.difference(set_2)) # 차집합
