# Python 자료형 가이드

## 1. 튜플(Tuple)

### 특징
- 순서가 있는 자료형 (인덱싱, 슬라이싱 가능)
- 중복 허용
- 수정 불가능(immutable)
- 소괄호 `()` 사용

### 기본 문법
```python
# 튜플 생성
tuple_1 = (1, 2, 3, 4, 5)

# 연산
tuple_1 + tuple_2    # 튜플 연결
tuple_1 * 3         # 튜플 반복

# 인덱싱과 슬라이싱
tuple_1[0]          # 첫 번째 요소
tuple_1[1:4]        # 1번째부터 4번째 전까지
tuple_1[-3:]        # 마지막 3개 요소
tuple_1[:5]         # 처음부터 5개 요소
```

## 2. 집합(Set)

### 특징
- 중복을 허용하지 않음
- 순서가 없음 (인덱싱 불가)
- 집합 연산 가능
- 중괄호 `{}` 사용

### 생성 방법
```python
set1 = {1, 2, 3, 4, 5}           # 중괄호로 생성
set2 = set([1, 2, 2, 3, 3, 4])   # set() 함수로 생성
```

### 집합 연산
```python
# 교집합
A & B                  # 연산자 방식
A.intersection(B)      # 메서드 방식

# 합집합
A | B                  # 연산자 방식
A.union(B)            # 메서드 방식

# 차집합
A - B                  # 연산자 방식
A.difference(B)        # 메서드 방식
```

## 3. 리스트(List)

### 특징
- 순서가 있는 자료형
- 중복 허용
- 수정 가능(mutable)
- 대괄호 `[]` 사용

### 기본 연산
```python
# 리스트 연결
list_1 + list_2

# 리스트 확장
list_1.append(list_2)   # 리스트를 하나의 요소로 추가
list_1.extend(list_2)   # 리스트의 요소들을 개별적으로 추가

# 리스트 반복
list_1 * 3
```

## 4. 자료형 변환

### Set ↔ List/Tuple 변환
```python
# 리스트/튜플 → Set (중복 제거)
set_from_list = set(my_list)
set_from_tuple = set(my_tuple)

# Set → 리스트
list_from_set = list(set_from_tuple)
```

## 주요 사용 팁
1. 중복 제거가 필요할 때 → Set 사용
2. 데이터 수정이 필요할 때 → List 사용
3. 변경되지 않아야 하는 데이터 → Tuple 사용
4. 집합 연산이 필요할 때 → Set 사용
5. 순서가 중요할 때 → List 또는 Tuple 사용