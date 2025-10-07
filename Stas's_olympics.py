def check_winners(scores, student_score):
    top_three = sorted(scores, reverse=True)[:3]
    if student_score >= top_three[-1]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

student_score = int(input("Введите балл Стаса: "))
n = int(input("Введите количество участников, не считая Стаса: "))
scores = []
for i in range(n):
    score = int(input(f"Введите балл участника {i+1}: "))
    scores.append(score)
scores.append(student_score)


check_winners(scores, student_score)