def analyze_marks_matrix(students, subjects, matrix):
    print("--- Performance Analytics Dashboard ---")

    num_students = len(students)
    num_subjects = len(subjects)

    # Initialize array placeholders for vertical aggregation columns
    subject_totals = [0] * num_subjects

    # Row-Wise Student Aggregation Loop
    for i in range(num_students):
        student_sum = 0
        for j in range(num_subjects):
            score = matrix[i][j]
            student_sum += score
            subject_totals[j] += score

        student_avg = student_sum / num_subjects
        print(f"Student: {students[i]:<8} | Total: {student_sum:<3} | Average: {student_avg:.2f}")

    print("\n--- Subject Metrics Trend ---")
    # Column-Wise Subject Analysis
    for j in range(num_subjects):
        subject_avg = subject_totals[j] / num_students
        status = "⚠️ Performance Warning" if subject_avg < 60 else "🏅 Safe"
        print(f"Subject: {subjects[j]:<12} | System Mean: {subject_avg:.2f} | Status: {status}")


# Matrix Setup Config
student_roster = ["Amit", "Bhavna", "Chirag"]
subject_list = ["Mathematics", "Physics", "Chemistry"]
marks_table = [
    [85, 78, 92],  # Amit
    [55, 62, 58],  # Bhavna
    [90, 88, 84]  # Chirag
]

analyze_marks_matrix(student_roster, subject_list, marks_table)
