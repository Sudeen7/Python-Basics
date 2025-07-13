"""
students grade manager:
starts while loop
takes student's name as input, requires marks obtained by the particular student in 3 subjects.
loop continues until 'exit' is given as input
finally, outputs name, marks in individual subjects, total marks, average marks and grade
"""
student = []


def calc_grade(marks):
    total = sum(marks)
    avg = total/len(marks)

    if avg >= 90 and avg < 100:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    elif avg < 60:
        grade = "F"

    return total, avg, grade


while True:
    name = input("Enter name of student (or type exit to stop): ").capitalize()
    if name.lower() == "exit":
        break
    mpy = int(input("\nEnter marks in Python: "))
    mjava = int(input("Enter marks in Java: "))
    mcs = int(input("Enter marks in C#: "))

    if mpy > 100 or mjava > 100 or mcs > 100:
        print("----Error! Marks cannot be greater than 100.----")
        break

    marks = (mpy, mjava, mcs)  # tuple

    total, avg, grade = calc_grade(marks)
    stdTuple = (name, marks, total, avg, grade)
    student.append(stdTuple)

print("Student Records: ")
for std in student:
    print(
        f"Name: {std[0]}, Marks: {std[1]}, Total Marks: {std[2]}, Average Marks: {std[3]}, Grade: {std[4]}")
