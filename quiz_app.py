# Quiz App - Tutorial for Learn IT

# Questions and possible answers as well as the define for which answer is correct. Make note of the formatting and placement of symbols
questions = [
    {
        "question": "besta rasen?",
        "options": ["A: vit", "B: svart", "C: gul", "D: brun"],
        "answer": "A"
    },
    {
        "question": "min favorit r6 opp",
        "options": ["A: jager", "B: ash", "C: sledg", "D: nokk"],
        "answer": "A"
    },
    {
        "question": "vilket instrument började jag spela i lågstadiet?",
        "options": ["A: gitar", "B: piano", "C: flöjt", "D: trummor"],
        "answer": "D"
    },
    {
        "question": "bästa snacket",
        "options": ["A: chips", "B: choklad", "C: mcflurry med sprit", "D: protein bar"],
        "answer": "c"
    },
    {
        "question": "vad heter min hund",
        "options": ["A: skit hund", "B: hund fan", "C: adopterade jävel", "D: sigge"],
        "answer": "D"
    },
    {
        "question": " favorit brain rot",
        "options": ["A: skibidi rizz", "B: you are my sunshine", "C: tiktok rizz party", "D: ohio"],
        "answer": "B"
    },
    {
        "question": "favorit movie trilogi",
        "options": ["A: jurasic park", "B: star wars", "C: indiana jones", "D: back to the future"],
        "answer": "A"
    },
    {
        "question": "när föddes jag",
        "options": ["A: januari", "B: october", "C: marsh", "D: december"],
        "answer": "B"
    },
    {
        "question": "favorit aktivitet",
        "options": ["A: supa skallen av mig", "B: gymma", "C: spela", "D: sova"],
        "answer": "A"
    },
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

# Run the quiz
run_quiz(questions)