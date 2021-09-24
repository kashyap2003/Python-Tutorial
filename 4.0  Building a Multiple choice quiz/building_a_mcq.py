from Question import Question

question_prompt = [
    "What colour are apple?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What colour are Banana?\n(a) Red\n(b) Yellow\n(c) Orange\n\n",
    "What colour are Strawberry?\n(a) Red\n(b) Purple\n(c) Green\n\n"

]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)

