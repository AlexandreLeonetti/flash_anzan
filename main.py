import tkinter as tk
from src.algo.hard_gen_class import HardNumberGenerator
from flash_anzan_app import FlashAnzanApp

def main():
    root = tk.Tk()
    hard_gen = HardNumberGenerator(num_count=5)
    app = FlashAnzanApp(root, num_count=2, display_time=500, number_generator=hard_gen)
    root.mainloop()

if __name__ == '__main__':
    main()
