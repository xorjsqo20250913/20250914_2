# 학생 관리 프로그램 - 성적 처리 및 석차 계산

# 학생 정보를 입력받는 함수
def input_student_info():
    students = []
    while True:
        name = input("학생 이름을 입력하세요 (종료하려면 q 입력): ")
        if name.lower() == 'q':
            break
        
        while True:
            try:
                score = int(input(f"{name}의 점수를 입력하세요 (0-100): "))
                if 0 <= score <= 100:
                    # 튜플로 학생 정보 저장 (이름, 점수)
                    students.append((name, score))
                    break
                else:
                    print("점수는 0에서 100 사이의 값이어야 합니다.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
    
    return tuple(students)  # 리스트를 튜플로 변환하여 반환

# 석차를 계산하는 함수
def calculate_ranks(students):
    # 점수에 따른 석차 계산
    ranks = []
    for i in range(len(students)):
        rank = 1
        for j in range(len(students)):
            if students[j][1] > students[i][1]:  # 다른 학생의 점수가 더 높으면
                rank += 1
        # 튜플로 학생 정보와 석차 저장 (이름, 점수, 석차)
        ranks.append(students[i] + (rank,))
    
    return tuple(ranks)  # 리스트를 튜플로 변환하여 반환

# 결과를 출력하는 함수
def print_results(ranked_students):
    print("\n=== 학생 성적 및 석차 ===")
    print("이름\t점수\t석차")
    print("-" * 20)
    
    # 석차를 기준으로 정렬된 새로운 튜플 생성
    sorted_students = tuple(sorted(ranked_students, key=lambda x: x[2]))
    
    for student in sorted_students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}")

def main():
    print("=== 학생 성적 관리 프로그램 ===")
    
    # 학생 정보 입력
    students = input_student_info()
    
    if not students:
        print("입력된 학생 정보가 없습니다.")
        return
    
    # 석차 계산
    ranked_students = calculate_ranks(students)
    
    # 결과 출력
    print_results(ranked_students)

if __name__ == "__main__":
    main()
