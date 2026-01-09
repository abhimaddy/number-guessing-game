# number-guessing-game
📌 Project Description

This is a simple and interactive Number Guessing Game built using Python.
In this game, the computer randomly selects a number between 1 and 100, and the user tries to guess the correct number.
After every guess, the program provides hints like “Too High” or “Too Low” until the correct number is guessed.

The game also keeps track of the number of attempts and calculates a score based on how quickly the user guesses the number.

This project is created to practice Python basics, logic building, and error handling.

🎮 How the Game Works

The computer generates a random number between 1 and 100

The user enters a number as a guess

The program:

Tells if the guess is too high or too low

Continues until the correct number is guessed

Total attempts are counted

A score is calculated based on attempts

✨ Features

Random number generation using random module

Infinite game loop until correct guess

Input validation (only numbers allowed)

Range validation (1 to 100)

Attempt counter

Score calculation system

User-friendly messages

Error handling using try-except

🧠 Concepts Used

Variables

Loops (while)

Conditional statements (if-elif-else)

Exception handling (try-except)

Python standard library (random)

User input handling

Basic game logic

🛠️ Technologies Used

Language: Python 3

Modules: random

Platform: Command Line Interface (CLI)

📂 Project Structure
number-guessing-game-python/
│
├── number_guessing_game.py
└── README.md

▶️ How to Run the Project
Step 1: Check Python Installation
python --version

Step 2: Clone the Repository
git clone https://github.com/abhimaddy/number-guessing-game.git

Step 3: Go to Project Directory
cd number-guessing-game

Step 4: Run the Program
python number_guessing_game.py

🧮 Scoring System
Attempts	Score
1	100
2 – 3	80
4 – 6	60
7 – 8	40
More than 8	20
📸 Sample Output
!!...Welcome To Number Guessing Game...!!
Guess a number between 1 to 100

Enter your guess : 50
📈 Too high! Try again!

Enter your guess : 25
📉 Too low! Try again!

Enter your guess : 37
🎉 WOOOHOO... CORRECT GUESS !!
My number was 37

Total attempts : 3
🏆 Your score : 80

📈 Future Improvements

Add maximum attempt limit

Add replay option (Play again?)

Save high score using file handling

Convert into GUI using Tkinter

Multiplayer mode

🎯 Learning Outcome

After completing this project, I gained hands-on experience in:

Writing clean and readable Python code

Implementing game logic

Handling user errors gracefully

Improving problem-solving skills

Understanding how scoring systems work

👨‍💻 Author

Abhishek Kumar Maddeshiya

GitHub: https://github.com/abhimaddy

Role: Python Developer (Beginner)

⭐ Support

If you like this project, please ⭐ star the repository on GitHub.
Feedback and suggestions are always welcome!

📜 License

This project is free to use for learning and educational purposes.
