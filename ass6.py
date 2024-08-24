def manage_student_database():
    students= []
    student_ids = 1

    while True:
        student_name= input("Please enter the studetn's name (or type 'stop' to finish):").strip()

        if student_name.lower() == 'stop':
            break

        if any(name for id, name in students if name == student_name):
             print("this name is already in the list ")
             continue 
        
        students.append((student_ids, student_name))
        student_ids += 1

    print("\nComplete List of Students (Tuples):")
    print(students)
    
    # Display each student's ID and name
    print("\nList of Students with IDs:")
    for id, name in students:
        print(f"ID: {id}, Name: {name}")
    
    # Calculate total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    total_name_length = sum(len(name) for id, name in students)
    print(f"Total length of all students names combined: {total_name_length}")

    if students:
        longest_name_student = max(students, key=lambda x: len(x[1]))
        shortest_name_student = min(students, key=lambda x: len(x[1]))
        print(f"The student with the longest name is: {longest_name_student[1]}")
        print(f"The student with the shortest name is: {shortest_name_student[1]}")
    else:
        print("no! studetns in the database.")

manage_student_database()