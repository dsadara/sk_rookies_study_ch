# 학생들의 성적을 입력 받아서 최고값, 최소값, 평균값, 특정 점수 이상의 count 프로그램

students = int(input("학생 수를 입력하세요: "))
score_list = []
goal = 80
count = 0

for i in range(students):
    score = int(input(f"{i+1}번째 학생 점수 입력: "))
    score_list.append(score)
    if score >= goal:
        count += 1


print(f"최대 점수: {max(score_list)}")
print(f"최소 점수: {min(score_list)}")
print(f"평균 점수: {sum(score_list)/students}")
print(f"{goal}점 이상 {count}명 입니다.")