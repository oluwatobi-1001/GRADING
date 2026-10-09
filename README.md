# GRADING

# 🎓 Grade Calculator

> *Dedicated to my secondary school days.*

A simple command-line program written in Python. Enter your name and your score, and it tells you your grade from A1 to F9, the same grading scale used in Nigerian secondary schools (WAEC).

Built as part of my 100 Days of Coding journey.

## Features

- Asks for your name and greets you by it in the result
- Takes your score as a whole number
- Gives your grade, from A1 (best) to F9 (lowest)
- Shows a different message for each grade, with emojis for the best and weakest results

## Grading scale

| Score | Grade | Message |
|---|---|---|
| 75 and above | A1 | Excellent 🎉 |
| 70 to 74 | B2 | Very Good |
| 65 to 69 | B3 | Good |
| 60 to 64 | C4 | Good |
| 55 to 59 | C5 | Good |
| 50 to 54 | C6 | Good |
| 45 to 49 | D7 | Oops |
| 40 to 44 | E8 | Oops |
| 39 and below | F9 | You can do better next time |

## How it works

1. The program asks for your name.
2. It asks for your score and converts it to a whole number with int().
3. It prints the score back to you.
4. It checks the score from the highest grade down to the lowest, and prints the first grade that matches.

flowchart TD
    A[Start] --> B[Enter your name]
    B --> C[Enter your score]
    C --> D{Score is 75 or more?}
    D -->|Yes| A1[A1: Excellent]
    D -->|No| E{70 or more?}
    E -->|Yes| B2[B2: Very Good]
    E -->|No| F{65 or more?}
    F -->|Yes| B3[B3: Good]
    F -->|No| G{60 or more?}
    G -->|Yes| C4[C4: Good]
    G -->|No| H{55 or more?}
    H -->|Yes| C5[C5: Good]
    H -->|No| I{50 or more?}
    I -->|Yes| C6[C6: Good]
    I -->|No| J{45 or more?}
    J -->|Yes| D7[D7: Oops]
    J -->|No| K{40 or more?}
    K -->|Yes| E8[E8: Oops]
    K -->|No| F9[F9: You can do better next time]
## Requirements

- Python 3
- No extra libraries needed

## How to run

1. Save the code as grading.py.
2. Open a terminal in the folder that contains the file.
3. Run:

python grading.py
## Example session

Enter your name:Ada
Ada,what's your score?67
67
Good Ada, you scored B3
## Ideas to improve it

- Reject scores below 0 or above 100
- Handle the case where someone types letters instead of a number, using try and except
- Let the program grade many students in one run, using a loop
- Add a space after "Excellent" and "Very Good" so the name does not stick to the word

## What I practised

- input() and int() to read a number from the user
- f-strings to put variables inside messages
- if, elif and else to choose between many outcomes
- Comparison operators >= and <=
- Why the order of conditions matters: checking from the highest score down

## Author

Oluwatobi Patience Oyelude
