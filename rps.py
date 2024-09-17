import random
import tkinter as tk
from tkinter import messagebox

# Function to handle the user choice
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    result = check_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. {result}")

# Function to check the winner
def check_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    
    if (user == "Rock" and computer == "Scissors") or \
       (user == "Paper" and computer == "Rock") or \
       (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

# Function to exit the game
def exit_game():
    root.quit()

# Setting up the GUI
root = tk.Tk()
root.title("RPS Game by balaji")
root.geometry("500x300")

# Adding a label
title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Helvetica", 18))
title_label.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Adding buttons for Rock, Paper, Scissors
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Exit button
exit_button = tk.Button(root, text="Exit", width=10, command=exit_game)
exit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
