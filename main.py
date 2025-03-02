import tkinter as tk
import sys
from src.algo.hard_gen_class import HardNumberGenerator
from flash_anzan_app import FlashAnzanApp

def main():
    delay = None

    for arg in sys.argv[1:]:
        if arg.startswith("-delay"):
            delay=int(arg.split("=")[1])

    if delay is None:
        return
    root = tk.Tk()
    hard_gen = HardNumberGenerator(num_count=10)
    app = FlashAnzanApp(root, num_count=2, display_time=delay, number_generator=hard_gen)
    root.mainloop()

if __name__ == '__main__':
    main()
