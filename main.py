import customtkinter
import tkinter
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

timerset = ''
imageset = ''
submitted_text = ''


def resolve_path(file_name):
    """ Resolve the path to the image file. """
    # Check if the path is already absolute
    if os.path.isabs(file_name):
        return file_name
    # Otherwise, consider it relative to the script's directory
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, file_name)


def start():
    frame2 = customtkinter.CTkFrame(master=root)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)

    # Resolve the full path of the image
    image_path = resolve_path(imageset)

    # Check if the image file exists before trying to open it
    if os.path.isfile(image_path):
        pil_image = Image.open(image_path)  # Open the image using PIL
        image_ctk = customtkinter.CTkImage(light_image=pil_image, size=(150, 150))  # Increase size of the image
        label = customtkinter.CTkLabel(master=frame2,
                                       text=f": {submitted_text}",  # Set the text
                                       image=image_ctk,
                                       compound='left',
                                       font=("Arial", 16))
        label.pack(pady=10, padx=10)
    else:
        error_label = customtkinter.CTkLabel(master=frame2,
                                             text="Image file not found",
                                             fg_color="red",
                                             font=("Arial", 16))  # Make error text visible
        error_label.pack(pady=10)


def submit():
    global timerset, imageset, submitted_text  # Use global variables
    timerset = int(timer.get())
    imageset = takeImage.get()
    submitted_text = takeText.get()  # Capture the submitted text



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Pymindr")
label.pack(pady=12, padx=10)

# What image do you want to use
takeImage = customtkinter.CTkEntry(master=frame, placeholder_text="Image desired")
takeImage.pack(pady=12, padx=10)

# How long should the program run
timer = customtkinter.CTkEntry(master=frame, placeholder_text="Pymindr timer")
timer.pack(pady=12, padx=10)

# Add a new entry for the text to be displayed
takeText = customtkinter.CTkEntry(master=frame, placeholder_text="Text to display next to image")
takeText.pack(pady=12, padx=10)

# Submit the image and text to global
subButton = customtkinter.CTkButton(master=frame, text="Submit", command=submit)
subButton.pack(pady=12, padx=10)

# Start button
startButton = customtkinter.CTkButton(master=frame, text="Start", command=start)
startButton.pack(pady=12, padx=10)

root.mainloop()
