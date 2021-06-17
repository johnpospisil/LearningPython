# Use While Loops when you want to repeat an action until a certain condition is met
i = 1

while i <= 10:
    print(i, end=' ')
    i += 1

print("\nDone with loop")

# Guessing Game
secret_word = "forge"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("\nGUESSING GAME")
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses. You lose.")
else:
    print("You guessed it!")
