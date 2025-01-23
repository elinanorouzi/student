#تابع افزودن اطلاعات دانشجو
def add_student():
    dic = {}
    while True:
        student_number = input("enter the student number: ")
        try:
            if not student_number:
                print("the student number must contain only numbers. please try again")
                continue
            number = float(student_number)
            if number in dic.keys():
                print("the student number is duplicate. please enter another student number.")
                continue
        except ValueError:
            print("number must be a number")
            continue

        key = number
        student_name = input("enter student name: ")
        scores = []
        while True:
            score = input("student score (enter 'done' to finish): ")
            if score.lower() == 'done':
                break
            try:
                score = float(score)
                if 0 <= score <= 20:
                    scores.append(score)
                else:
                    print("enter a number between 0, 20")
            except ValueError:
                print("please enter a valid number")
        
        DATE = {"name": student_name, "scores": scores}
        dic[key] = DATE
        more_student = input("do you want to add another student? (yes/no): ")
        if more_student.lower() != "yes":
            break
    return dic

#تابع نمايش اطلاعات دانشجو
def display_students(dic):
    if not dic:
        print("no students have been added")
        return

    for student_number, student_info in dic.items():
        print(f"student number:{student_number}, student info: {student_info}")



#تابع ميانگين نمرات دانشجو
def score_averages(dic):
    stu_number = input("enter the student number: ")
    try:
        student_number = float(stu_number)
        if student_number in dic:
            student_DATA = dic[student_number]
            scores = student_DATA.get("scores", [])
            if scores:
                average = sum(scores) / len(scores)
                print(f"the student with number {student_number}: average score is {average:.2f}")
            else:
                print("no score has been recorded for the student")
        else:
            print("no student was found with this number")
    except ValueError:
        print("number must be a number")

#تابع جستوجو و بروزرساني اطلاعات
def search_and_update(dic):
    student_number = input("enter student number: ")
    try:
        student_number = float(student_number)
        if student_number in dic:
            print(f"the student information with number {student_number}: {dic[student_number]}")
            add = input("do you want to update this student?(yes/no): ")
            if add.lower() == "yes":
                student_DATA = dic[student_number]
                scores = student_DATA.get("scores", [])

                while True:
                    score = input("student score (enter 'done' to finish): ")
                    if score.lower() == 'done':
                        break
                    try:
                        score = float(score)
                        if 0 <= score <= 20:
                            scores.append(score)
                        else:
                            print("enter a number between 0, 20")
                    except ValueError:
                        print("enter a valid number")
                student_DATA["scores"] = scores 
                return dic
        else:
            print("no student was found with this number")
    except ValueError:
        print("number must be a number")
    return dic


dic = {}

#حلقه براي منوي اصلي
while True:
    print("1. add_student")
    print("2. display_students")
    print("3. score_averages")
    print("4. search_and_update")
    print("5. exit")
    choice = input("choice a number: ")

    if choice == "1":
        dic = add_student()
    elif choice == "2":
        display_students(dic)
    elif choice == "3":
        score_averages(dic)
    elif choice == "4":
        dic = search_and_update(dic)
    elif choice == "5":
        print("the program is over")
        break
    else:
        print("enter a valid number")
