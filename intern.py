import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize variables
current_player = 'X'
board = ['' for _ in range(9)]

# Function to check for a win or tie
def check_winner():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    
    if '' not in board:
        return 'Tie'
    
    return None

# Function to handle button click
def button_click(index):
    global current_player
    
    if board[index] == '':
        board[index] = current_player
        buttons[index].config(text=current_player, state='disabled')
        
        winner = check_winner()
        if winner:
            if winner == 'Tie':
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Function to reset the game
def reset_game():
    global board, current_player
    board = ['' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text='', state='normal')

# Create buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text='', font=('normal', 40), width=5, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the Tkinter event loop
root.mainloop()
