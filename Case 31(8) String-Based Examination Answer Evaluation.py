def score_exam(answer_key, student_submissions):
    print("--- Grading Registry Evaluation ---\n")

    for record in student_submissions:
        name, response_str = record
        correct = 0
        incorrect = 0
        unanswered = 0

        for idx in range(len(answer_key)):
            student_choice = response_str[idx]
            correct_choice = answer_key[idx]

            if student_choice == 'X':
                unanswered += 1
            elif student_choice == correct_choice:
                correct += 1
            else:
                incorrect += 1

        # Grading Metrics Formula: +4 for Correct, -1 for Mistake, 0 for Blanks
        final_score = (correct * 4) + (incorrect * -1)
        max_possible = len(answer_key) * 4

        print(f"Candidate : {name}")
        print(f" -> Summary: [{correct} Correct] | [{incorrect} Incorrect] | [{unanswered} Skipped]")
        print(f" -> Final Scaled Score: {final_score} / {max_possible}\n")


# Evaluation execution
key = "ABCDABCDAB"
submissions = [
    ("John Doe", "ABCDBBCDAA"),  # Some mistakes
    ("Jane Smith", "ABCDXABCDX")  # Unanswered skips present
]
score_exam(key, submissions)
