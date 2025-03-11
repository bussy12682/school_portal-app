import tkinter as tk

# Global variable for counting clicks
count = 0
app = tk.Tk()
app.title("Student Portal")

def click():
    """Handles button click and transitions after 3 clicks"""
    global count
    count += 1
    label.config(text=f"Clicks: {count}")

    if count == 3:  # Transition to the next page after 3 clicks
        ask_user_info()
def app_colour():
    tk.Label(app, app_colour="Green:",)
    app_colour()
def ask_user_info():
    """Clears the screen and asks for student details"""
    for widget in app.winfo_children():
        widget.destroy()  # Clear current page

    tk.Label(app, text="Enter your first name:", font=("Arial", 14)).pack()
    first_name_entry = tk.Entry(app)
    first_name_entry.pack()

    tk.Label(app, text="Enter your last name:", font=("Arial", 14)).pack()
    last_name_entry = tk.Entry(app)
    last_name_entry.pack()

    tk.Label(app, text="Enter your school name:", font=("Arial", 14)).pack()
    school_entry = tk.Entry(app)
    school_entry.pack()

    tk.Label(app, text="Enter your gender (Male/Female):", font=("Arial", 14)).pack()
    gender_entry = tk.Entry(app)
    gender_entry.pack()

    tk.Label(app, text="Enter your Exam/Registration Number:", font=("Arial", 14)).pack()
    exam_number_entry = tk.Entry(app)
    exam_number_entry.pack()

    tk.Label(app, text="Enter your Seat Number:", font=("Arial", 14)).pack()
    seat_number_entry = tk.Entry(app)
    seat_number_entry.pack()

    def submit_student_details():
        """Collects student details and moves to score entry"""
        student_data = {
            "Full Name": first_name_entry.get().title() + " " + last_name_entry.get().title(),
            "School": school_entry.get().title(),
            "Gender": gender_entry.get().title(),
            "Exam Number": exam_number_entry.get(),
            "Seat Number": seat_number_entry.get()
        }
        ask_student_scores(student_data)  # Move to score entry

    tk.Button(app, text="Next", command=submit_student_details).pack()

def ask_student_scores(student_data):
    """Clears screen and asks for scores"""
    for widget in app.winfo_children():
        widget.destroy()  # Clear current page

    tk.Label(app, text="Enter your scores (1 - 100):", font=("Arial", 14)).pack()

    subjects = ["English", "Mathematics", "Physics", "Chemistry", "ICT"]
    score_entries = {}

    for subject in subjects:
        tk.Label(app, text=f"{subject}:", font=("Arial", 12)).pack()
        entry = tk.Entry(app)
        entry.pack()
        score_entries[subject] = entry

    def submit_scores():
        """Collect scores, calculate grades, and display results"""
        scores = {subject: int(score_entries[subject].get()) for subject in subjects}
        cumulative_score = sum(scores.values())
        average_score = cumulative_score / len(subjects)
        status = "Pass" if average_score >= 50 else "Fail"

        show_results(student_data, scores, average_score, status)

    tk.Button(app, text="Submit", command=submit_scores).pack()

def show_results(student_data, scores, average_score, status):
    """Displays final student results"""
    for widget in app.winfo_children():
        widget.destroy()  # Clear current page

    tk.Label(app, text="Student Result Summary", font=("Arial", 16, "bold")).pack()
    for key, value in student_data.items():
        tk.Label(app, text=f"{key}: {value}", font=("Arial", 12)).pack()

    tk.Label(app, text="Scores:", font=("Arial", 14, "bold")).pack()
    for subject, score in scores.items():
        tk.Label(app, text=f"{subject}: {score}", font=("Arial", 12)).pack()

    tk.Label(app, text=f"Average Score: {average_score:.2f}", font=("Arial", 14)).pack()
    tk.Label(app, text=f"Status: {status}", font=("Arial", 14, "bold"), fg="green" if status == "Pass" else "red").pack()

    tk.Button(app, text="Exit", command=app.quit).pack()

# Initial GUI layout
label = tk.Label(app, text="Clicks: 0", font=("Arial", 16))
label.pack()

button = tk.Button(app, text="Enter!(3x)", command=click)
button.pack()

app.mainloop()

#BY ENOCH OMONIYI
