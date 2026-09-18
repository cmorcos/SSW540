def fullTime(student):
    return student[2] >= 3  # first name, last name, # of courses. [2] takes the 3rd value aka # of courses and checks if it's enough for full time aka 3


def main():
    for i in range(9):  # same as last assignment for inputting 9 student names
        first = input("first name: ")
        last = input("last name: ")
        courses = int(input("num of courses: "))
        student = (first, last, courses)

        status = "full time" if fullTime(student) else "part time"  # checks course requirement for each student
        print(student[0], student[1], "-", status)


main()