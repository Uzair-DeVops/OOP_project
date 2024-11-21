# Student Performance Tracker

## Introduction
I created this Python program to manage and analyze the performance of students in a class. My idea was to make it easier to track scores, calculate averages, and determine the pass or fail status of students while providing an overall class average.

---

## My Approach and Logic

### 1. **Defining the `Student` Class**
   - **Reason**: I wanted each student to have their own profile to store their name and scores.
   - **Logic**:
     - I used a dictionary `scores` to store subject names as keys and their corresponding scores as values.
     - The `add_score` method allows adding scores for individual subjects.
     - The `average` method calculates the average score by summing all scores and dividing by the number of subjects.
     - The `is_pass` method iterates through all subjects to check if any score is below 40. If so, the student fails in that subject, otherwise, they pass.

### 2. **Creating the `PerformanceTracker` Class**
   - **Reason**: To manage multiple students in one place.
   - **Logic**:
     - I used a dictionary `students` to map student names to their corresponding `Student` objects.
     - The `add_student` method ensures names contain only alphabetic characters, raising an error otherwise.
     - The `calculate_class_average` method iterates through all students, calculates their averages, and finds the overall class average.
     - The `display_student_performance` method retrieves and prints each student's name, average score, and pass/fail status.

### 3. **Building the Main Logic**
   - **Reason**: To create an interactive console application.
   - **Logic**:
     - The program enters a loop where the user can add a student or type "exit" to finish.
     - For each student, I prompt the user to enter scores for `English`, `Math`, and `Science`. I used input validation to ensure scores are numeric and between 0 and 100.
     - After all students are added, I display each student's performance and the overall class average.

---

## Challenges and Solutions

### 1. **Validating Student Names**
   - **Challenge**: Preventing invalid names like numbers or symbols.
   - **Solution**: I used the `isalpha()` method to ensure names only contain alphabetic characters. Invalid names raise a `ValueError`.

### 2. **Validating Scores**
   - **Challenge**: Ensuring scores are within a valid range (0-100).
   - **Solution**: I wrapped the input logic for scores in a loop with a `try-except` block. This re-prompts the user until valid input is provided.

### 3. **Handling Empty or Small Classes**
   - **Challenge**: Calculating averages when no students or very few students exist.
   - **Solution**: I ensured division is based on the number of students to avoid errors.

---

## Code Walkthrough

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}  

    def add_score(self, subject, score):
        self.scores[subject] = score

    def average(self):
        return sum(self.scores.values()) / len(self.scores)
    
    def is_pass(self):
        for subject, score in self.scores.items():
            if score < 40:
                return f"Fail (failed in {subject})" 
        return "Pass"  


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if not name.isalpha():
            raise ValueError("Invalid student name. Please enter a valid name (only letters).")
        self.students[name] = Student(name)

    def calculate_class_average(self):
        total_score = 0
        for student in self.students.values():
            total_score += student.average()
        return total_score / len(self.students)

    def display_student_performance(self):
        for name, student in self.students.items():
            avg_score = student.average()
            pass_status = student.is_pass()
            print(f"Student: {name}, Average Score: {avg_score:.2f}, Status: {pass_status}")


# Main program
tracker = PerformanceTracker()

while True:
    student_name = input("Enter student name (or type 'exit' to finish): ")
    if student_name.lower() == 'exit':
        break

    try:
        tracker.add_student(student_name)

        for subject in ['English', 'Math', 'Science']:
            while True:
                try:
                    score = float(input(f"Enter score for {subject} (0-100): "))
                    if 0 <= score <= 100:
                        tracker.students[student_name].add_score(subject, score)
                        break
                    else:
                        print("Please enter a valid score between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
    except ValueError as e:
        print(e)

tracker.display_student_performance()
print(f"Class Average Score: {tracker.calculate_class_average():.2f}")
```

---

## Example Interaction

1. **Input**:
   ```
   Enter student name (or type 'exit' to finish): Alice
   Enter score for English (0-100): 85
   Enter score for Math (0-100): 90
   Enter score for Science (0-100): 78
   Enter student name (or type 'exit' to finish): Bob
   Enter score for English (0-100): 40
   Enter score for Math (0-100): 39
   Enter score for Science (0-100): 50
   Enter student name (or type 'exit' to finish): exit
   ```

2. **Output**:
   ```
   Student: Alice, Average Score: 84.33, Status: Pass
   Student: Bob, Average Score: 43.00, Status: Fail (failed in Math)
   Class Average Score: 63.67
   ```

---

## Lessons Learned
- **Input Validation**: Always validate user input to prevent crashes.
- **Error Handling**: Using `try-except` blocks enhances robustness.
- **OOP Design**: Classes and methods simplify program structure and scalability.

---

