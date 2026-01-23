# Part 1

quiz = float(input("What's your quiz average (0-100): "))
lab = float(input("What's your lab average (0-100): "))
midterm = float(input("What's your midterm average (0-100): "))
final_exam = float(input("What's your final exam average (0-100): "))

final_grade = (quiz * 0.20) + (lab * 0.30) + (midterm * 0.30) + (final_exam * 0.30)

print(float(final_grade))

# Part 2
print("Is the student eligible for honors? ", 
final_grade >= 90 and midterm >= 80 and lab >= 80
)

# Part 3
print((quiz + lab) / 2 > midterm)
print(final_exam >= midterm)
print(quiz != lab)
print(not (final_grade < 75))
