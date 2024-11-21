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
        if  not name.isalpha():
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


