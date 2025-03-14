import tkinter as tk
import random
import os
from PIL import Image, ImageTk 

import pygame
import threading
import time

# Initialize pygame mixer
pygame.mixer.init()
def play_countdown():
    countdown_sound = pygame.mixer.Sound("src/SOUNDPS/START01.wav")
    countdown_sound.set_volume(0.3)
    countdown_sound.play()

def play_countdown_async():
    threading.Thread(target=play_countdown, daemon=True).start()

def play_beep():
    beep_sound = pygame.mixer.Sound("src/SOUNDPS/bip1.wav")
    beep_sound.set_volume(0.5)  # Set volume (0.0 = mute, 1.0 = max)
    beep_sound.play()

def play_beep_async():
    threading.Thread(target=play_beep, daemon=True).start()

class DefaultNumberGenerator:
    def __init__(self, num_count):
        self.num_count = num_count

    def generate(self):
        return [random.randint(10, 99) for _ in range(self.num_count)]


class FlashAnzanApp:
    def __init__(self, root, num_count=3, display_time=2000, number_generator=None):
        self.num_count = num_count
        self.number_generator = number_generator or DefaultNumberGenerator(self.num_count)
        self.root = root
        self.root.title("Flash Anzan")
        # Fix the window size (half the screen width or fixed width as desired)
        half_width = 800
        window_height = 700
        self.root.geometry(f"{half_width}x{window_height}")
        self.root.configure(bg="grey")

        self.display_time = display_time  # Display time per number in milliseconds

        self.numbers = []
        self.current_index = 0
        self.displayed_images = []  # To keep references to PhotoImage labels

        # Load images for digits 0-9
        self.digit_images = self.load_digit_images()

        # Build the user interface
        self.setup_ui()


    def generate_numbers(self):
        return [random.randint(10, 99) for _ in range(self.num_count)]

    def load_digit_images(self):
        """Load images for digits 0-9 from the src/png/ folder and resize them."""
        images = {}
        # Specify a scaling factor or a target size, e.g., 80% of the original
        scale_factor = 0.8  # or set a fixed size: target_width, target_height = (50, 70)
        for digit in "0123456789":
            path = os.path.join("src", "png", f"{digit}M.PNG")

            # Open the image using PIL
            pil_image = Image.open(path)
            
            # Option 1: Scale by a factor (80% of original size)
            new_width = int(pil_image.width * scale_factor)
            new_height = int(pil_image.height * scale_factor)
            #pil_image = pil_image.resize((new_width, new_height), Image.ANTIALIAS)
            pil_image = pil_image.resize((new_width, new_height), Image.LANCZOS)

            # Convert back to Tkinter PhotoImage
            images[digit] = ImageTk.PhotoImage(pil_image)
        return images

    def setup_ui(self):
        """Set up the UI components."""
        self.digit_frame = tk.Frame(self.root, bg="green")
        self.digit_frame.pack(pady=(120,20))

        self.prompt_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="grey")
        self.prompt_label.pack()

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="grey" )
        self.result_label.pack(pady=20)

        self.check_button = tk.Button(self.root, text="Check Answer", command=self.check_answer, font=("Helvetica", 16))
        self.start_button = tk.Button(self.root, text="Start Flash Anzan", command=self.start_flash_anzan, font=("Helvetica", 16))

        self.replay_button = tk.Button(self.root, text="Re try", command=self.start_flash_anzan_with_same_serie, font=("Helvetica", 16) )

        self.start_button.pack(pady=20)

    def clear_digit_frame(self):
        """Remove all digit image labels from the digit frame."""
        for widget in self.digit_frame.winfo_children():
            widget.destroy()
        self.displayed_images = []

    def start_flash_anzan(self):
        """Generates random numbers and begins the flash sequence."""
        # Hide or reset the UI elements
        self.start_button.pack_forget()
        self.replay_button.pack_forget()
        self.result_label.config(text="")
        self.prompt_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        self.clear_digit_frame()
        self.digit_frame.pack(pady=(120,20))

        # try changing background color
        self.root.configure(bg="black")
        self.digit_frame.configure(bg="black")
        self.prompt_label.configure(bg="black")
        self.result_label.configure(bg="black")

        #self.numbers = [random.randint(10, 99) for _ in range(self.num_count)]
        #self.numbers = self.generate_numbers()
        self.numbers = self.number_generator.generate()

        self.current_index = 0
        # hey chatgpt, check this out :
        play_countdown()# this sound lasts about a second
        self.root.after(1900, self.display_next_number)
        #self.display_next_number()

    def start_flash_anzan_with_same_serie(self):
        """Generates random numbers and begins the flash sequence."""
        # Hide or reset the UI elements
        self.start_button.pack_forget()
        self.replay_button.pack_forget()
        self.result_label.config(text="")
        self.prompt_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        self.clear_digit_frame()
        self.digit_frame.pack(pady=(120,20))

        # try changing background color
        self.root.configure(bg="black")
        self.digit_frame.configure(bg="black")
        self.prompt_label.configure(bg="black")
        self.result_label.configure(bg="black")

        self.current_index = 0
        play_countdown()# this sound lasts about a second
        self.root.after(1900, self.display_next_number)
        #self.display_next_number()

    # flicking numbers 
    def display_next_number(self):
        """Displays each number for a set time before showing the input prompt."""
        if self.current_index < len(self.numbers):
            self.clear_digit_frame()
            play_beep_async()  # Or play_beep_async() if using threading and playsound
            # Convert the current number to a string and display its digit images.
            num_str = str(self.numbers[self.current_index])
            for digit in num_str:
                img_label = tk.Label(self.digit_frame, image=self.digit_images[digit], bg="black")
                img_label.pack(side=tk.LEFT, padx=2)
                self.displayed_images.append(img_label)  # Keep a reference
            self.current_index += 1
            # After half the display time, clear the digits so they disappear.
            self.root.after(int(self.display_time*0.8), self.clear_digit_frame)
            # After the full display time, show the next number.
            self.root.after(self.display_time, self.display_next_number)
        # entry of answer 
        else:
            # hey chatGPT
            self.clear_digit_frame()
            self.prompt_label.config(text="Enter the sum of the numbers:")#
            self.answer_entry.pack(pady=5)
            self.answer_entry.focus_set()  # Automatically set focus to the entry field
            self.answer_entry.bind("<Return>", lambda event: self.check_answer())  # Bind Enter key to check_answer

            self.check_button.pack(pady=5)
            # try changing background color
            self.root.configure(bg="grey")
            self.digit_frame.configure(bg="grey")
            self.prompt_label.configure(bg="grey")
            self.result_label.configure(bg="grey")
            self.digit_frame.pack(pady=(20))


    def check_answer(self):
        try:
            user_sum = int(self.answer_entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            return

        correct_sum = sum(self.numbers)
        if user_sum == correct_sum:
            self.result_label.config(text="Correct! Well done.")
            # remove enter the number, entry field, check answer
            self.check_button.pack_forget()
            self.prompt_label.pack_forget()
            self.answer_entry.pack_forget()

        else:
            self.result_label.config(text=f"Incorrect. The correct sum is {correct_sum}.")
            # cleaning entry interface after submitting answer
            self.check_button.pack_forget()
            self.prompt_label.pack_forget()
            self.answer_entry.pack_forget()
        
        # Show both buttons so user can either replay or start a new series
        self.start_button.pack(pady=20)
        self.replay_button.pack(pady=20)
