import customtkinter as ctk
from config.config import images_open, colors

def toggle_appearance(main, button, mode):
    if mode == "dark":
        mode = "light"
        ctk.set_appearance_mode("light")
        button.configure(image=images_open.moon)
        main.configure(fg_color=colors.background_light)
    else:
        mode = "dark"
        ctk.set_appearance_mode("dark")
        button.configure(image=images_open.sun)
        main.configure(fg_color=colors.background)
    return mode