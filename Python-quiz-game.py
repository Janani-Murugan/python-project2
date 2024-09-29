# python quiz game

import time

class Question:
    
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def display(self):
        print(self.prompt)
        for option in self.options:
            print(option)

class Quiz:
    
    def __init__(self, questions):
        self.questions = questions
        self.guesses = []
        self.score = 0

    def getuserguess(self):
        start_time = time.time()  # Start timing
        while True:
            try:
                guess = input("Enter (A, B, C, D): ").upper()
                if guess not in ["A", "B", "C", "D"]:
                    raise ValueError("Invalid input! Please enter A, B, C, or D.")
                elapsed_time = time.time() - start_time  # Calculate elapsed time
                print(f"You took {elapsed_time:.2f} seconds to answer.")
                return guess  
            except ValueError as e:
                print(e)

    def calculatescore(self):
        self.score = sum(1 for guess, question in zip(self.guesses, self.questions) if guess == question.answer)
        return int(self.score / len(self.questions) * 100)

    def displayresults(self):
        print("_______________________")
        print("RESULTS:")
        
        print("Answers: ", end="")
        for question in self.questions:
            print(question.answer, end=" ")
        print()

        print("Guesses: ", end="")
        for guess in self.guesses:
            print(guess, end=" ")
        print()

        score_percentage = self.calculatescore()
        print(f"Your score is: {score_percentage}%")

def main():
    questions = [
        Question(
            "Which of the following is not a key concept in OOP?:",
            ["A. Inheritance", "B. Polymorphism", "C. Multiprocessing", "D. Encapsulation"],
            "C"
        ),
        Question(
            "In Python, an object is:",
            ["A. A real-world entity", "B. A collection of data and methods", "C. Always physical", "D. Only data"],
            "B"
        ),
        Question(
            "In Python, how is the constructor defined for a class?:",
            ["A. init()", "B. construct()", "C. __init__()", "D. __construct__()"],
            "C"
        ),
        Question(
            "What is the concept of inheriting properties of one class into another class?:",
            ["A. Polymorphism", "B. Multiprocessing", "C. Encapsulation", "D. Inheritance"],
            "D"
        ),
        Question(
            "Which method gets called when an object is deleted?:",
            ["A. __del__", "B. __delete__", "C. __remove__", "D. __exit__"],
            "A"
        )
    ]

    quiz = Quiz(questions)

    for question in quiz.questions:
        print("_______________________")
        question.display()
        
        guess = quiz.getuserguess()
        quiz.guesses.append(guess)
        
        if guess == question.answer:
            print("CORRECT!")
        else:
            print(f"INCORRECT! The correct answer was {question.answer}.")

    quiz.displayresults()

print("Welcome!")
if __name__ == "__main__":
    main()
