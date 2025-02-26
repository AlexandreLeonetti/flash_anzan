import time
import os
import random

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def flash_anzan(num_count=5, display_time=0.5):
    """
    Displays a series of random two-digit numbers briefly,
    then asks the user to compute their sum.
    """
    # Generate a list of random two-digit numbers.
    numbers = [random.randint(10, 99) for _ in range(num_count)]
    
    print("Get ready to memorize the numbers!")
    time.sleep(1)
    
    # Display each number for a short period.
    for number in numbers:
        clear_screen()
        print(f"{number}")
        time.sleep(display_time)
    
    # Clear the screen before prompting for input.
    clear_screen()
    try:
        user_input = int(input("Enter the sum of the numbers: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    correct_sum = sum(numbers)
    if user_input == correct_sum:
        print("Correct! Well done.")
    else:
        print(f"Incorrect. The correct sum is {correct_sum}.")

if __name__ == "__main__":
    flash_anzan(5,1)
