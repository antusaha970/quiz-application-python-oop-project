class Quiz:
    def __init__(self, subject_name, total_question) -> None:
        self.subject_name = subject_name
        self.total_question = total_question
        self.question = []  # object of question class

    def add_question(self, question):
        self.question.append(question)
        print("Question added")
