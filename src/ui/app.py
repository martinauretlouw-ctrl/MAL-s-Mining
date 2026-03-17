# Main Tkinter UI application

import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Tkinter UI")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.run()