from user import Admin, Student
from quiz import Quiz
from question import Question
from colorama import Fore, Back, Style


def runSystem():
    admin = Admin("admin")
    while True:
        print(Fore.LIGHTYELLOW_EX + "<--- Welcome --->")
        print("Please setup question first then student can give quiz")
        print("1. Continue as admin")
        print("2. Continue as Student")
        print("3. Exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            name = input("Please enter your name: ")
            print(f"<--- Welcome {name} --->")
            while True:
                print("1 > setup quiz")
                print("2 > Delete quiz")
                print("3 > Exit")
                cmd = int(input("Please enter your choice: "))
                if cmd == 1:
                    subject_name = input("Enter subject name: ")
                    total_question = int(
                        input("How many question you want setup: "))
                    quiz = Quiz(subject_name, total_question)
                    for _ in range(total_question):
                        qus = input("Question: ")
                        op1 = input("Option 1: ")
                        op2 = input("Option 2: ")
                        ans = int(input("Ans 1 or 2: "))
                        question = Question(qus, op1, op2, ans)
                        quiz.add_question(question)
                    time = int(input("How many seconds will quiz occur: "))
                    admin.add_quiz(subject_name, quiz)
                    admin.add_time(subject_name, time)

                elif cmd == 2:
                    subject_name = input("Enter subject name: ")
                    admin.delete_quiz(subject_name)
                else:
                    break

        elif choice == 2:
            name = input("Enter your name: ")
            student = Student(name)
            while True:
                print(Fore.RED + f"<--- welcome {name} --->")
                print("1. Give quiz")
                print("2. View  previews quiz result")
                print("3. Exit")
                op = int(input("Select and option: "))
                if op == 1:
                    while True:
                        print(Fore.RED +
                              "Please select the subject id to give quiz: \nFor exit press 9")

                        admin.show_quiz_option()
                        sub_id = int(input("enter you option: "))
                        if sub_id == 9:
                            break
                        else:
                            result = admin.take_quiz(sub_id)
                            student.add_result(result)
                elif op == 2:
                    student.view_result()
                else:
                    break
        else:
            break


runSystem()
