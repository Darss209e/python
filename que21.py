questions = {
    "capital of india ?": "delhi",
    "2+2?":"4",
    "color of sky?":"blue"
}
score = 0
for question in questions:
    user_ans = input(question+" ")

    if user_ans.lower() == questions[question]:
        print("correct!")
        score+=1
    else:
        print("wrong!")
print("you got",score,"out of",len(questions))
