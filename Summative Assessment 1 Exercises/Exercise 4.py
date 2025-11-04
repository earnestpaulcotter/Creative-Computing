# Score variables
Questions = 10
FinalScore = 0

# Defs
def correctanswer():
    global FinalScore
    print("Your answer is correct! You get 1 point!")
    FinalScore += 1

def wronganswer():
    print("Incorrect! Sorry, you get no points!")

# List of countries and their capitals
quiz_data = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Italy", "Rome"),
    ("Spain", "Madrid"),
    ("United Kingdom", "London"),
    ("Netherlands", "Amsterdam"),
    ("Belgium", "City of Brussels"),
    ("Sweden", "Stockholm"),
    ("Poland", "Warsaw"),
    ("Austria", "Vienna")
]

# Ask all questions in a loop
user_answers = []  # to store the user's responses

for country, capital in quiz_data:
    answer = input(f"What is the capital of {country}?: ")
    user_answers.append(answer)
    if answer.lower() == capital.lower():
        correctanswer()
    else:
        wronganswer()

# Final score output
print("\nYour final score is", FinalScore, "out of", Questions)
print("Your answers were:", user_answers)
print("Answer key:", [capital for _, capital in quiz_data])