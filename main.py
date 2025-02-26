import tkinter as tk
import random

def start_flash_anzan():
    """Generates random numbers and begins the flash sequence."""
    global numbers, current_index
    # Hide the start button and reset the UI
    start_button.pack_forget()
    result_label.config(text="")
    prompt_label.config(text="")
    answer_entry.delete(0, tk.END)
    answer_entry.pack_forget()
    check_button.pack_forget()

    # Generate a list of random two-digit numbers.
    numbers = [random.randint(10, 99) for _ in range(num_count)]
    current_index = 0
    display_next_number()

def display_next_number():
    """Displays each number for a set time before showing the input prompt."""
    global current_index
    if current_index < len(numbers):
        # Update the label to show the next number.
        number_label.config(text=str(numbers[current_index]))
        current_index += 1
        # Schedule the next number after display_time milliseconds.
        root.after(display_time, display_next_number)
    else:
        # End of the sequence: clear the number and show input field.
        number_label.config(text="")
        prompt_label.config(text="Enter the sum of the numbers:")
        answer_entry.pack(pady=5)
        check_button.pack(pady=5)

def check_answer():
    """Compares the user's input to the correct sum."""
    try:
        user_sum = int(answer_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return
    
    correct_sum = sum(numbers)
    if user_sum == correct_sum:
        result_label.config(text="Correct! Well done.")
    else:
        result_label.config(text=f"Incorrect. The correct sum is {correct_sum}.")
    # Show the start button again so the user can try another round.
    start_button.pack(pady=20)

# Create the main window.
root = tk.Tk()
root.title("Flash Anzan")
# Fix the window size to half the screen width.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
half_width = 400#screen_width // 2
# You can set the window height as you prefer; here it's set to 400 pixels.
window_height = 400
root.geometry(f"{half_width}x{window_height}")

# Parameters for the flash session.
num_count = 5        # Number of numbers to display.
display_time = 500   # Time each number is displayed (in milliseconds).

# Global variables.
numbers = []
current_index = 0

# Create UI Elements.
number_label = tk.Label(root, text="", font=("Helvetica", 48))
number_label.pack(pady=20)

prompt_label = tk.Label(root, text="", font=("Helvetica", 16))
prompt_label.pack()

answer_entry = tk.Entry(root, font=("Helvetica", 16))

check_button = tk.Button(root, text="Check Answer", command=check_answer, font=("Helvetica", 16))

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

start_button = tk.Button(root, text="Start Flash Anzan", command=start_flash_anzan, font=("Helvetica", 16))
start_button.pack(pady=20)

# Start the Tkinter event loop.
root.mainloop()
