# Welcome to my “rhythm guessing challenge” for music people.. The idea, the music “theory” and most of the code is by me.
# I needed help with the random-function, the margin logic and twice debugging because I did not understand
# what the console wanted to tell me. This was then done by Gemini AI – I hope that's fine:)


import time
import random

## Start
bpm = random.randint(60, 160)
base_quarter = 60000 / bpm

print("🎶 RHYTHM CALCULATION CHALLENGE 🎶")
time.sleep(1)
print("Note: To calculate the ms use bpm/60000. But try to play without a calculator.. It's more fun then!")
time.sleep(2)
print(f"\n[SYSTEM] Current Tempo: {bpm} BPM")

# INPUT: Difficulty
print("\nSelect Difficulty: [1] Easy or [2] Pro")
diff_choice = input(">> ")

if diff_choice == "2":
    margin = 5
    print("Pro mode active🎯")
else:
    margin = 30
    print("Easy mode active🌊")

# INPUT: Note Division
print("\nSelect the note division to calculate:")
print("A) 1/4 Note")
print("B) 1/8 Note")
print("C) 1/8 Dotted Note")
note_choice = input(">> ").upper().strip()

if note_choice == "B":
    correct_ms = base_quarter / 2
    note_name = "1/8 Note"
elif note_choice == "C":
    correct_ms = (base_quarter / 2) * 1.5
    note_name = "1/8 Dotted Note"
else:
    correct_ms = base_quarter
    note_name = "1/4 Note"

## ROUND 1
# INPUT: First Guess
while True:
    try:
        print(f"\n[TRY 1] Guess the delay for a {note_name} (in ms):")
        guess1 = float(input(">> "))
        if 1 <= guess1 <= 3000:
            break
        else:
            print("❌ OUT OF RANGE: Enter a value between 1 and 3000ms.")
    except ValueError:
        print("❌ ERROR: Please enter a number.")

print("Analyzing signal... 📡")
time.sleep(1.2)

diff_score1 = abs(guess1 - correct_ms)

# Results
if diff_score1 <= margin:
    print(f" Yeah! You got it on the first try. Target was {correct_ms:.2f}ms.")
else:
    # hint (close/far)
    if diff_score1 < 100:
        proximity = "You're very close!"
    else:
        proximity = "Far away!"

    # hint (higher/lower)
    if guess1 > correct_ms:
        direction = "too high!"
    else:
        direction = "too low!"

    print(f"❌ {proximity} Your guess was {direction}.")
    print("SECOND CHANCE")

    # INPUT: Second Guess
    while True:
        try:
            print("Enter your second guess:")
            guess2 = float(input(">> "))
            if 1 <= guess2 <= 3000:
                break
            else:
                print("❌ OUT OF RANGE: Stay between 1 and 3000ms.")
        except ValueError:
            print("❌ ERROR: Enter a number.")

    print("Re-calculating... 🔄")
    time.sleep(1)

    diff_score2 = abs(guess2 - correct_ms)

    # Final Result
    if diff_score2 <= margin:
        print(f"✅ SAVED! The target was {correct_ms:.2f}ms.")
    else:
        print(f"💀 GAME OVER. The correct answer was {correct_ms:.2f}ms.")

print("\n--- SESSION TERMINATED ---")
