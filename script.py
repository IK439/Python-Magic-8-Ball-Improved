import random

# Function randomly picks and returns a Magic 8-Ball answer
def get_answer():
    answers = [
        "Yes, everything seems fine!",
        "No, something is off.",
        "Almost there, keep checking.",
        "It looks like it works.",
        "Not quite, try again later.",
        "All systems go!",
        "Hmm… maybe, needs testing.",
        "Absolutely working!",
        "Check again, might be a glitch.",
        "Yes, it's running perfectly."
    ]

    # Generate a random index based on the length of the list and return the value at the index
    random_index = random.randint(0, len(answers) - 1)
    return answers[random_index]

# Hard-coded name and question
name = "IK439"
question = "Is this working?"

# Print name with question and Magic 8-Ball's answer
if question == "":
    print("Ask me is this working.")
else:
    if name == "":
        print("Question:", question)
    else:
        print(name, "asks:", question)

    answer = get_answer()
    print("\nMagic 8-Ball's answer:", answer)