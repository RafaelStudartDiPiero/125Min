import tkinter as tk
from tkinter import font as tkfont
from .welcomepage import WelcomePage
from .planejarrota import PlanejarRota
from .instrucoes import Instrucoes
from .faleconosco import FaleConosco
from .atualizardados import AtualizarDados


class MainFrame(tk.Tk):
    """
    Container class responsible for contain other pages and responsible for changing pages in the same Window.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the main controller.
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.titlefont = tkfont.Font(
            family='Times New Roman', size=24, slant="roman")
        self.descriptionfont = tkfont.Font(
            family='Times New Roman', size=14, slant="roman")
        self.buttonfont = tkfont.Font(
            family='Times New Roman', slant="roman")
        self.buttonbg = "#FFFFFF"
        self.pagesbg = "#E2E2E2"

        container = tk.Frame()
        container.grid(row=0, column=0, sticky="nesw")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.id = tk.StringVar()
        self.id.set("Rafael")

        self.pages = {}

        for p in (WelcomePage, PlanejarRota, Instrucoes, FaleConosco, AtualizarDados):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.pages[page_name] = frame

        self.up_frame("WelcomePage")

    def up_frame(self, page_name):
        """"""
        page = self.pages[page_name]
        page.tkraise()
