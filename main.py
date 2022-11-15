import tkinter as tk
from pages.mainframe import MainFrame
from VRP import run_otimization

if __name__ == "__main__":
    # run_otimization()
    app = MainFrame()
    app.geometry('800x700')
    app.mainloop()