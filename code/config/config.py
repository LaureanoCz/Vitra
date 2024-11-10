import customtkinter as ctk
from PIL import Image

# <-- ------------| Config colors| ------------ -->
class colors:
    background = "#0f0f12"
    background_light = "#ffffff"
    button = "#9555f7"
    button_hover = "#7d33ea"
    entry = ""
    text = "#f9f5ff"
    border = ""

# <-- ------| Config elements - dark mode | ------ -->
class button_style(ctk.CTkButton):
    def __init__(self, master=None, text='', command=None):
        super().__init__(master=master, text=text, command=command)
        self.configure(
            width=50,
            height=50,
            corner_radius=5,
            hover_color=colors.button_hover,
            fg_color=colors.button,
            font=('Arial', 25)
        )
        self.grid(padx=5, pady=5, sticky='nsew')

# <-- ------| Config images | ------ -->
class images_open:
    moon_image = Image.open("code/images/moon.png")
    moon = ctk.CTkImage(moon_image, size=(25, 25))

    sun_image = Image.open("code/images/sun.png")
    sun = ctk.CTkImage(sun_image, size=(25, 25))