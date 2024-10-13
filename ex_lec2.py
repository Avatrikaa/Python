from random import randint

print("Welcome to the Simple Multiplication Quiz!")
n = randint(1, 10)
print(f"You will be given {n} multiplication problems to solve.")
scr = 0

for i in range(n):
    a = randint(1, 10)
    b = randint(1, 10)
    print(f"Problem {i+1}: What is {a} x {b}?")
    ans = input("Your answer: ")
    correct_answer = a*b
    if int(ans) == correct_answer:
        scr += 1
        print("Correct!")
    else: print(f"Incorrect. The Correct answer was {correct_answer}")

print(f"You scored {scr} out of {n}.")
