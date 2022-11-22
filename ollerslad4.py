import random
secret_words = ["Boris","Tony","Gordon","Margaret","Theresa"]
word = random.choice(secret_words)
lives = 5
guesses = []
answer = []
def print_answer(word):
    correct_guess = ""
    for letter in word:
        if letter in answer:
            correct_guess += letter
        else:
            correct_guess += "_"
    print(correct_guess)


def guess(x):
    global lives
    if x is int:

        print("letters not numbers mate!")

    correct = False#
    i = 0
    for letter in word:

        if x == letter:
            correct = True

            answer.append(x)


        i += 1
    if correct == False:

        lives = lives - 1

        guesses.append(x)

        print("Sadly not correct, your Current Lives are", lives, "and your guesses thusfar", guesses)



def game(word):
    running = True
    while running:
        x = input("Take a guess")
        guess(x)
        print_answer(word)
        if lives == 0:
            running = False
            print("bad luck lad, maybe next time ;), shame about that capitol letter")
        if len(answer) == len(word):
            running = False
            print("Fucking legend")

game(word)