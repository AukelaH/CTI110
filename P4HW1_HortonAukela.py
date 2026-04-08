# Aukela Horton
# 04/07/2026
# P4HW1
# This program collects scores, validates them, drops the lowest score,
# calculates the average, and displays the letter grade.

"""
Pseudocode:
1. Ask the user how many scores they want to enter.
2. Create an empty list to store the scores.
3. Use a loop to collect each score.
4. Check if each score is valid.
5. If the score is invalid, ask again until a valid score is entered.
6. Add each valid score to the list.
7. Find the lowest score.
8. Remove the lowest score from the list.
9. Calculate the average of the remaining scores.
10. Determine the letter grade based on the average.
11. Display the results.
"""

num_scores = int(input("How many scores do you want to enter? "))

score_list = []

for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    score_list.append(score)

lowest_score = min(score_list)
score_list.remove(lowest_score)

average_score = sum(score_list) / len(score_list)

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print()
print("------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("--------------------------------")