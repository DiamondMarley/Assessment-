import random

# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

def instruction():
    print('''

**** Instructions ****

To begin, choose the number of questions you'd like to answer!

You will be given questions about squares and rectangles. 

Your goal is to try to guess the area and perimeter of square 
and rectangle. 

 Good luck.   

    ''')

# Formula to calculate area
def calculate_area(shape, length, width=None):
    if shape == "square":
        return length * length
    else:  # rectangle
        return length * width

# Formula to calculate perimeter
def calculate_perimeter(shape, length, width=None):
    if shape == "square":
        return 4 * length
    else:  # rectangle
        return 2 * (length + width)

# Main routine starts here

print("📚📚📚Welcome to the Area Perimeter Quiz ↕️↕️↕️ ")
print()

want_instructions = yes_no("Do you want to read the instructions?")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

    want_instructions = yes_no("Do you want to read the instructions?")

    # checks users enter yes (y) or no (n)
    if want_instructions == "yes":
        instruction()

# Generate a question
def generate_question(q_number):
    shape = random.choice(["square", "rectangle"])
    question_type = random.choice(["area", "perimeter"])

    # Generate side lengths
    length = random.randint(1, 20)
    width = length if shape == "square" else random.randint(1, 20)

    # Create the question
    if shape == "square":
        question_text = f"Q{q_number}: What is the {question_type} of a square with side length {length}?"
    else:
        question_text = f"Q{q_number}: What is the {question_type} of a rectangle with length {length} and width {width}?"

    # Calculate the correct answer
    if question_type == "area":
        correct_answer = calculate_area(shape, length, width)
    else:
        correct_answer = calculate_perimeter(shape, length, width)

    return question_text, correct_answer

# Display the quiz history
def show_history(quiz_log):
    print("\n=== QUIZ HISTORY ===")
    for record in quiz_log:
        print(record['question'])
        if record['correct']:
            print(f"✅ Correct! Answer: {record['correct_answer']}")
        else:
            print(f"❌ Incorrect. Your answer: {record['user_answer']} | Correct answer: {record['correct_answer']}")
        print("-" * 50)

# Main quiz
def start_quiz():
    print("You will be asked questions about squares and rectangles.\n")

    # Ask user how many questions to generate
    while True:
        try:
            total_questions = int(input("How many questions would you like to answer? "))
            if total_questions > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid! Please enter a integer.")

    # Initialize score and history list
    score = 0
    quiz_history = []

    # Loop through each question
    for q_num in range(1, total_questions + 1):
        question, correct_answer = generate_question(q_num)
        print("\n" + question)

        # Get user answer
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid! Please enter a number.")

        # Check if the answer is correct
        is_correct = user_answer == correct_answer
        if is_correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {correct_answer}.")

        # Save to quiz history
        quiz_history.append({
            'question': question,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'correct': is_correct
        })
    # Quiz Statistics
    print("\n=== QUIZ STATISTICS ===")
    print(f"Questions answered: {total_questions}")
    print(f"Correct answers: {score}")
    print(f"Incorrect answers: {total_questions - score}")

    # Ask if user wants to see full history
    see_history = input("Would you like to see your quiz history? (yes/no): ").strip().lower()
    if see_history in ["yes", "y"]:
        show_history(quiz_history)

if __name__ == "__main__":
    start_quiz()

print("💿💿💿Thanks for playing💿💿💿")
print()
