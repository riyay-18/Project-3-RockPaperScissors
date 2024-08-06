import tkinter as tk
import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"


def play(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    
    if result == "You win!":
        scores["User"] += 1
    elif result == "You lose!":
        scores["Computer"] += 1
    
    
    user_score_label.config(text=f"User Score: {scores['User']}")
    computer_score_label.config(text=f"Computer Score: {scores['Computer']}")


def reset_game():
    scores["User"] = 0
    scores["Computer"] = 0
    user_score_label.config(text="User Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    result_label.config(text="")


root = tk.Tk()
root.title("Rock, Paper, Scissors")


scores = {"User": 0, "Computer": 0}


tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)


tk.Button(root, text="Rock", command=lambda: play("Rock"), width=10).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper"), width=10).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("Scissors"), width=10).pack(pady=5)


result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)


user_score_label = tk.Label(root, text="User Score: 0", font=("Arial", 14))
user_score_label.pack(pady=5)

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 14))
computer_score_label.pack(pady=5)


tk.Button(root, text="Reset Scores", command=reset_game, width=10).pack(pady=20)


root.mainloop()