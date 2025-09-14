# Python 기본 문법 가이드

## 1. 조건문 (Conditional Statements)

### 1.1 기본 조건문 (if-elif-else)
```python
# 기본 구조
if 조건1:
    실행문1
elif 조건2:
    실행문2
else:
    실행문3

# 실제 예제 - 성적 처리
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
```

### 1.2 중첩 조건문 (Nested if)
```python
# 기본 구조
if 조건1:
    if 조건2:
        실행문1
    else:
        실행문2

# 실제 예제 - 숫자 분석
num = 15
if num >= 10:
    if num % 3 == 0:
        print("10이상의 3의 배수")
    else:
        print("10이상의 수")
```

### 1.3 논리 연산자와 조건문
```python
# and 연산자
if num % 2 == 0 and num % 3 == 0:
    print("2와 3의 공배수")

# or 연산자
if age <= 7 or age >= 65:
    print("무료 입장")

# in 연산자
list_1 = [1, 2, 3, 4, 5]
if 2 in list_1:
    print("2가 리스트에 있음")
```

## 2. 자료형 (Data Types)

### 2.1 튜플(Tuple)
```python
# 특징
# - 순서가 있음 (인덱싱, 슬라이싱 가능)
# - 중복 허용
# - 수정 불가능(immutable)

# 생성
tuple_1 = (1, 2, 3, 4, 5)

# 연산
print(tuple_1 + (6, 7))  # 연결
print(tuple_1 * 2)      # 반복
print(tuple_1[0])       # 인덱싱
print(tuple_1[1:4])     # 슬라이싱
```

### 2.2 집합(Set)
```python
# 특징
# - 중복 불가
# - 순서 없음
# - 집합 연산 가능

# 생성
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 집합 연산
print(set1 & set2)  # 교집합
print(set1 | set2)  # 합집합
print(set1 - set2)  # 차집합
```

### 2.3 딕셔너리(Dictionary)
```python
# 특징
# - 키-값 쌍으로 데이터 저장
# - 키는 중복 불가, 값은 중복 가능
# - 순서 없음

# 기본 사용
student = {
    "name": "홍길동",
    "age": 20,
    "subjects": {
        "국어": 90,
        "영어": 85,
        "수학": 95
    }
}

# 접근과 수정
print(student["name"])           # 값 접근
student["age"] = 21             # 값 수정
student["gender"] = "남"         # 새 항목 추가
```

### 2.4 중첩 딕셔너리 활용
```python
# 복잡한 데이터 구조
company = {
    "부서": {
        "개발팀": {
            "직원1": {
                "이름": "김개발",
                "나이": 28,
                "스킬": ["Python", "Java"]
            },
            "직원2": {
                "이름": "박코딩",
                "나이": 32,
                "스킬": ["JavaScript", "HTML", "CSS"]
            }
        }
    }
}
```

## 3. 실전 프로그래밍 예제

### 3.1 학생 성적 관리 프로그램
```python
students = []

# 학생 정보 입력
while True:
    name = input("이름 (종료: q): ")
    if name.lower() == 'q':
        break
    
    score = int(input("점수: "))
    students.append((name, score))  # 튜플로 저장

# 석차 계산
ranks = []
for i in range(len(students)):
    rank = 1
    for j in range(len(students)):
        if students[j][1] > students[i][1]:
            rank += 1
    ranks.append((students[i][0], students[i][1], rank))

# 결과 출력
for name, score, rank in sorted(ranks, key=lambda x: x[2]):
    print(f"{name}: {score}점 (석차: {rank})")
```

## 4. 프로그래밍 팁

### 4.1 자료형 선택 가이드
- **튜플**: 변경되지 않는 데이터 시퀀스 (예: 좌표값, RGB 색상값)
- **집합**: 중복 제거가 필요하거나 집합 연산이 필요할 때
- **딕셔너리**: 키-값 쌍으로 데이터를 구조화할 때
- **리스트**: 수정 가능한 순서 있는 데이터 모음이 필요할 때

### 4.2 조건문 작성 팁
- 복잡한 조건은 여러 단계로 나누기
- 가장 중요하거나 자주 발생하는 조건을 먼저 검사
- 조건문 내부에 너무 많은 중첩을 피하기
- 논리 연산자를 활용하여 조건을 간단히 표현

### 4.3 코드 구조화
- 관련 있는 데이터는 딕셔너리로 구조화
- 반복되는 코드는 함수로 모듈화
- 복잡한 로직은 단계별로 주석 달기
- 직관적인 변수명과 함수명 사용