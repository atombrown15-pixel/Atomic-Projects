# This program greets students and calculates their WAEC/NECO grades
print('Hello!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)

# Ask for the student's exam score
print('What is your exam score (0-100)?')
myScore = int(input()) # Converts the typed input into a number

# Grading Logic using the WAEC scale
if myScore >= 75 and myScore <= 100:
    grade = "A1 (Excellent)"
elif myScore >= 70:
    grade = "B2 (Very Good)"
elif myScore >= 65:
    grade = "B3 (Good)"
elif myScore >= 60:
    grade = "C4 (Credit)"
elif myScore >= 55:
    grade = "C5 (Credit)"
elif myScore >= 50:
    grade = "C6 (Credit)"
elif myScore >= 45:
    grade = "D7 (Pass)"
elif myScore >= 40:
    grade = "E8 (Pass)"
elif myScore >= 0:
    grade = "F9 (Fail)"
else:
    grade = "Invalid Score! (Must be between 0 and 100)"

# Output the final result
print(f"\nStudent Name: {myName}")
print(f"Exam Score: {myScore}/100")
print(f"Final Grade: {grade}")
