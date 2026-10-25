import tkinter as tk
import random

# Initialize scores
wins = 0
losses = 0
ties = 0

def play(choice):
    global wins, losses, ties
    options = ["Rock", "Paper", "Scissors"]
    computer = random.choice(options)
    
    if choice == computer:
        result = "It's a Tie!"
        ties += 1
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissors" and computer == "Paper"):
        result = "You Win!"
        wins += 1
    else:
        result = "You Lose!"
        losses += 1
    
    # Update result and score labels
    label_result.config(text=f"Computer: {computer}. {result}")
    label_score.config(text=f"Wins: {wins} | Losses: {losses} | Ties: {ties}")

root = tk.Tk()
root.title("Rock Paper Scissors")

label_result = tk.Label(root, text="Choose your move!")
label_result.pack(pady=20)

# Score display label
label_score = tk.Label(root, text="Wins: 0 | Losses: 0 | Ties: 0")
label_score.pack(pady=10)

for move in ["Rock", "Paper ", "Scissors "]:
    tk.Button(root, text=move, width=15, pady=10, 
              command=lambda m=move.split()[0]: play(m)).pack(pady=10)

root.mainloop()