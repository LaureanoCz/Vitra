import customtkinter as ctk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window.geometry(f'{width}x{height}+{int((screen_width - width) / 2)}+{int((screen_height - height) / 2)}')