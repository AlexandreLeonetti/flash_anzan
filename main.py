import tkinter as tk
from flash_anzan_app import FlashAnzanApp

def main():
    root = tk.Tk()
    app = FlashAnzanApp(root, num_count=5, display_time=2000)
    root.mainloop()

if __name__ == '__main__':
    main()
