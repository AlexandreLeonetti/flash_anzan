import tkinter as tk
import random
import os
from PIL import Image, ImageTk 

class FlashAnzanApp:
    def __init__(self, root, num_count=3, display_time=2000):
        self.root = root
        self.root.title("Flash Anzan")

        # Fix the window size (half the screen width or fixed width as desired)
        half_width = 800
        window_height = 700
        self.root.geometry(f"{half_width}x{window_height}")
        self.root.configure(bg="grey")

        self.num_count = num_count        # Number of numbers to display
        self.display_time = display_time  # Display time per number in milliseconds

        self.numbers = []
        self.current_index = 0
        self.displayed_images = []  # To keep references to PhotoImage labels

        # Load images for digits 0-9
        self.digit_images = self.load_digit_images()

        # Build the user interface
        self.setup_ui()

    def old_load_digit_images(self):
        """Load images for digits 0-9 from the src/png/ folder."""
        images = {}
        for digit in "0123456789":
            path = os.path.join("src", "png", f"{digit}M.PNG")
            images[digit] = tk.PhotoImage(file=path)
        return images

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

            
            # Option 2: Alternatively, you can set a fixed size:
            # pil_image = pil_image.resize((50, 70), Image.ANTIALIAS)
            
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
        self.result_label.config(text="")
        self.prompt_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        self.clear_digit_frame()
        self.digit_frame.pack(pady=(320,20))

        # try changing background color
        self.root.configure(bg="black")
        self.digit_frame.configure(bg="black")
        self.prompt_label.configure(bg="black")
        self.result_label.configure(bg="black")

        # Generate random two-digit numbers.
        self.numbers = [random.randint(10, 99) for _ in range(self.num_count)]
        self.current_index = 0
        self.display_next_number()

    def display_next_number(self):
        """Displays each number for a set time before showing the input prompt."""
        if self.current_index < len(self.numbers):
            self.clear_digit_frame()
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
            
        else:
            self.clear_digit_frame()
            self.prompt_label.config(text="Enter the sum of the numbers:")
            self.answer_entry.pack(pady=5)
            self.check_button.pack(pady=5)
            # try changing background color
            self.root.configure(bg="grey")
            self.digit_frame.configure(bg="grey")
            self.prompt_label.configure(bg="grey")
            self.result_label.configure(bg="grey")
            self.digit_frame.pack(pady=(20))

    def check_answer(self):
        """Compares the user's input to the correct sum."""
        try:
            user_sum = int(self.answer_entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            return

        correct_sum = sum(self.numbers)
        if user_sum == correct_sum:
            self.result_label.config(text="Correct! Well done.")
        else:
            self.result_label.config(text=f"Incorrect. The correct sum is {correct_sum}.")
        self.start_button.pack(pady=20)
