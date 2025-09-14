#  tuple,list,set
#  tuple: 순서가 있고, 중복을 허용한다, 근데 한번 만들만 수정이 불가하다(immutable)
tuple_1 = (1,2,3,4,5,1,2,3)
#list는 대괄호, tuple은 소괄호, set은 중괄호
tuple_2 = (10,20)
print('tuple_1 + tuple_2 = ', tuple_1 + tuple_2) 
print('tuple_1 * 3 = ', tuple_1 * 3)  # 반복
print('tuple_1[0] = ', tuple_1[0]) # 인덱싱
print('tuple_1[0:3] = ', tuple_1[1:4]) # 슬라이싱 1부터 4전까지
print('튜플의 개수는 =', len(tuple_1))
print("마지막 튜플의 값 =", tuple_1[len(tuple_1)-1])
# 튜플의 데이터 중에서 마지막 3개를 출력 
print("마지막 튜플의 값= ", tuple_1 [-3:]) #:하고 비워두면 끝까지
# 튜플의 데이터 중에서 처음 3개를 출력
print("처음 5개의 값= ", tuple_1 [:5])



# tuple. append(10) # error
# tuple은 수정이 불가하다

