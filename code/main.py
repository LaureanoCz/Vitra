import customtkinter as ctk
from util.center_window import center_window
from config.config import button_style, images_open, colors
from util.change_mode import toggle_appearance

# <-- ------------| Config window | ------------ -->

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

mode = "dark"

main = ctk.CTk(fg_color=colors.background)
main.title("Vitra - Welcome :)")

window_width = 400
window_height = 300

center_window(main, window_width, window_height)

# <-- ------------| elements | ------------ -->
button = ctk.CTkButton(main, text='', image=images_open.sun, width=50, height=50, corner_radius=5, hover=None, fg_color='transparent', font=('Arial', 25), command=lambda: toggle_appearance(main, button, mode))
button.pack(pady=5, padx=5)

main.mainloop()