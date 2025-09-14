#  tuple,list,set
#  tuple: 순서가 있고, 중복을 허용한다, 근데 한번 만들만 수정이 불가하다(immutable)
tuple_1 = (1,2,3,4,5,1,2,3)
#list는 대괄호, tuple은 소괄호, set은 중괄호
tuple_2 = (10,20)
print('tuple_1 + tuple_2 = ', tuple_1 + tuple_2) 
print('tuple_1 * 3 = ', tuple_1 * 3)  # 반복
print('tuple_1[0] = ', tuple_1[0]) # 인덱싱
print('tuple_1[0:3] = ', tuple_1[1:4]) # 슬라이싱 1부터 4전까지
# tuple. append(10) # error
# tuple은 수정이 불가하다

