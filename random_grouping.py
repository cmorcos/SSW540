students = []   # array to hold listed names

# used ai to teach about try and except since i wasnt as familiar with it for exception handling
while len(students) < 9:    # create input for list and check exceptions, only current issue is that "-" may be flagged as wrong even if it's correct, not sure if that needed to be specified given the context of the assignment
    try:
        first_name = input("input first name: ")
        last_name = input("input last name: ")
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError("invalid name, try again")
        students.append((first_name, last_name))
    except ValueError as valueError:
        print(valueError)

# alphabetical sort
def get_last_name(student):
    return student[1]
sorted_students = sorted(students, key=get_last_name)

# check for sorted last names being in the same group as those next to it
def last_name_check(student_1, student_2, sorted_students):
    index1 = sorted_students.index(student_1)
    index2= sorted_students.index(student_2)
    return abs(index1 - index2) == 1            # absolute value to check if they're directly next to the other in the original list

# check hypothetical addition to group
def group_check(group_candidate, group, sorted_students):
    for member in group:
        if last_name_check(group_candidate, member, sorted_students):
            return True
    return False        # else
    
# make groups
def group_maker(students, sorted_students):
    groupA = []
    groupB = []
    groupC = []

    for student in students:    # check if group criteria is met
        if len(groupA) < 3 and not group_check(student, groupA, sorted_students):
            groupA.append(student)
        elif len(groupB) < 3 and not group_check(student, groupB, sorted_students):
            groupB.append(student)
        elif len(groupC) < 3 and not group_check(student, groupC, sorted_students):
            groupC.append(student)
        else:
            if len(groupA) < 3:
                groupA.append(student)
            elif len(groupB) < 3:
                groupB.append(student)
            else:
                groupC.append(student)

    return [groupA, groupB, groupC]

groups = group_maker(students, sorted_students)

# used ai for this block for formatting purpose
for i, group in enumerate(groups):
    print(f"Group {i + 1}:")
    for student in group:
        print(f"{student[0]} {student[1]}")
    print()  # blank line between groups