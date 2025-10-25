score = 75

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 50 <= score < 70:
    grade = "C"
else:
    grade = "Ungraded"

print(f"You got {grade} for scoring {score}.")