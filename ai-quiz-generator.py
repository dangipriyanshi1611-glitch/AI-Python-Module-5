# ============================================================
# AI QUIZ GENERATOR
# ============================================================

import random


# Quiz questions
quiz_data = {

    "python": [
        {
            "question": "Which language is Python?",
            "options": [
                "A. Programming Language",
                "B. Operating System",
                "C. Database",
                "D. Web Browser"
            ],
            "answer": "A"
        },

        {
            "question": "Which symbol is used for comments in Python?",
            "options": [
                "A. //",
                "B. #",
                "C. <!-- -->",
                "D. **"
            ],
            "answer": "B"
        },

        {
            "question": "Which function is used to display output in Python?",
            "options": [
                "A. display()",
                "B. output()",
                "C. print()",
                "D. show()"
            ],
            "answer": "C"
        },

        {
            "question": "Which data type is used to store True or False?",
            "options": [
                "A. String",
                "B. Integer",
                "C. Boolean",
                "D. Float"
            ],
            "answer": "C"
        },

        {
            "question": "Which symbol is used to create a list in Python?",
            "options": [
                "A. ()",
                "B. {}",
                "C. []",
                "D. <>"
            ],
            "answer": "C"
        }
    ],


    "machine learning": [
        {
            "question": "What is Machine Learning?",
            "options": [
                "A. A type of computer hardware",
                "B. A method where computers learn from data",
                "C. A programming language",
                "D. An operating system"
            ],
            "answer": "B"
        },

        {
            "question": "Which type of learning uses labelled data?",
            "options": [
                "A. Supervised Learning",
                "B. Unsupervised Learning",
                "C. Reinforcement Learning",
                "D. Random Learning"
            ],
            "answer": "A"
        },

        {
            "question": "House price prediction is an example of:",
            "options": [
                "A. Classification",
                "B. Regression",
                "C. Clustering",
                "D. Sorting"
            ],
            "answer": "B"
        },

        {
            "question": "Which is an example of Machine Learning?",
            "options": [
                "A. Spam email detection",
                "B. Calculator",
                "C. Text editor",
                "D. File manager"
            ],
            "answer": "A"
        },

        {
            "question": "Which type of value does regression usually predict?",
            "options": [
                "A. Continuous numerical value",
                "B. Only text",
                "C. Only images",
                "D. File names"
            ],
            "answer": "A"
        }
    ],


    "artificial intelligence": [
        {
            "question": "What does AI stand for?",
            "options": [
                "A. Automatic Internet",
                "B. Artificial Intelligence",
                "C. Advanced Information",
                "D. Automated Input"
            ],
            "answer": "B"
        },

        {
            "question": "Which of these is an example of AI?",
            "options": [
                "A. Voice Assistant",
                "B. Keyboard",
                "C. Mouse",
                "D. Monitor"
            ],
            "answer": "A"
        },

        {
            "question": "Which technology is a part of AI?",
            "options": [
                "A. Machine Learning",
                "B. HTML only",
                "C. CSS only",
                "D. MS Word"
            ],
            "answer": "A"
        },

        {
            "question": "AI systems are designed to:",
            "options": [
                "A. Perform intelligent tasks",
                "B. Only store files",
                "C. Only print documents",
                "D. Only browse websites"
            ],
            "answer": "A"
        },

        {
            "question": "Which is an AI chatbot?",
            "options": [
                "A. ChatGPT",
                "B. Calculator",
                "C. Notepad",
                "D. Paint"
            ],
            "answer": "A"
        }
    ]
}


def start_quiz(topic):

    questions = quiz_data[topic]

    # Shuffle questions
    random.shuffle(questions)

    score = 0

    print("\n")
    print("=" * 60)
    print("                    AI QUIZ")
    print("=" * 60)

    for number, question in enumerate(questions, 1):

        print("\nQuestion", number)
        print(question["question"])

        for option in question["options"]:
            print(option)

        while True:

            user_answer = input(
                "\nEnter your answer (A/B/C/D): "
            ).upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("Please enter A, B, C or D.")

        if user_answer == question["answer"]:

            print("Correct! ✓")
            score += 1

        else:

            print(
                "Wrong! ✗ Correct answer:",
                question["answer"]
            )

    percentage = (score / len(questions)) * 100

    print("\n")
    print("=" * 60)
    print("                  QUIZ RESULT")
    print("=" * 60)

    print("Score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")

    if percentage == 100:
        print("Excellent! Perfect score!")

    elif percentage >= 80:
        print("Great job!")

    elif percentage >= 60:
        print("Good work! Keep practicing.")

    elif percentage >= 40:
        print("You can improve. Keep learning.")

    else:
        print("Keep practicing and try again!")

    print("=" * 60)


def main():

    print("=" * 60)
    print("                 AI QUIZ GENERATOR")
    print("=" * 60)

    print("\nChoose a topic:")

    print("1. Python")
    print("2. Machine Learning")
    print("3. Artificial Intelligence")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        start_quiz("python")

    elif choice == "2":
        start_quiz("machine learning")

    elif choice == "3":
        start_quiz("artificial intelligence")

    else:
        print("\nInvalid choice.")
        print("Please select 1, 2 or 3.")


main()