from abc import ABC
from colorama import Fore, Back, Style
from quiztimer import QuizTimer


class User(ABC):
    def __init__(self, name) -> None:
        self.name = name


class Admin(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.available_quiz = []  # {"english": [object of quiz]}
        self.time_limit = []  # {"english": 5000s}

    def add_quiz(self, subject_name, quiz):
        self.available_quiz.append({subject_name: quiz})

    def add_time(self, sub, time):
        self.time_limit.append({sub: time})

    def delete_quiz(self, subject_name):
        for quiz in self.available_quiz:
            for k, v in quiz.items():
                if k == subject_name:
                    self.available_quiz.remove(quiz)
                    print("Quiz removed for this subject")
                    return
        print("No Quiz found for this subject")

    def take_quiz(self, id):
        result = 0
        totalQuestion = 0
        key = None
        timeLimit = 60
        subject = self.available_quiz[id]
        for s, quiz in subject.items():
            key = s
            totalQuestion = len(quiz.question)

        for timeObj in self.time_limit:
            for sub_name, time in timeObj.items():
                if sub_name == key:
                    timeLimit = time
                    break

        quiz_timer = QuizTimer(timeLimit)  # Set time limit
        for s, quiz in subject.items():
            quiz_timer.start_timer()   # Start the timer in parallel
            for question in quiz.question:
                print(f"Q. {question.question}")
                print(f"1. {question.option_1}")
                print(f"2. {question.option_2}")
                ans = int(input("Enter ans: "))
                if ans == question.ans:
                    result += 1
                if quiz_timer.is_time_up():
                    print("Time's up!!!")
                    break
        print(Fore.GREEN + f"You scored: {result} out of {totalQuestion}")
        return {key, result}

    def show_quiz_option(self):
        print(f"id\tsubject")
        for id, quiz in enumerate(self.available_quiz):
            for k, _ in quiz.items():
                print(f"{id}\t{k}")


class Student(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.result = []  # {"english":result}

    def add_result(self, result):
        self.result.append(result)

    def view_result(self):
        if len(self.result) > 0:
            print("your result: ")
            for result in self.result:
                print(result)
        else:
            print("No result available")
