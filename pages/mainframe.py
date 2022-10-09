import tkinter as tk
from tkinter import font as tkfont
from .welcomepage import WelcomePage
from .pageone import PageOne


class MainFrame(tk.Tk):
    """
    Container class responsible for contain other pages and responsible for changing pages in the same Window.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the main controller.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(
            family='Verdana', size=12, weight="bold", slant="roman")

        container = tk.Frame()
        container.grid(row=0, column=0, sticky="nesw")

        self.id = tk.StringVar()
        self.id.set("Rafael")

        self.pages = {}

        for p in (WelcomePage, PageOne):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.pages[page_name] = frame
        
        self.up_frame("WelcomePage")
    
    def up_frame(self, page_name):
        """"""
        page = self.pages[page_name]
        page.tkraise()

