from tkinter import Tk


def create_app():
    tk = Tk()
    tk.geometry('400x400')
    tk.title('GUI shop')
    return tk


tk = create_app()