import tkinter as tk
from tkinter import messagebox
import pyttsx3 
# Function to handle the convert button click
def on_convert(event=None):
    input_text = text_box.get()  # Get the text from the input box
    if input_text.strip():
        # converted_text = input_text.upper()  # Example: Convert input text to uppercase
        # messagebox.showinfo("Converted Text", f"Converted Text: {converted_text}")
        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        engine=pyttsx3.init("sapi5")
        voices=engine.getProperty("voices")
        engine.setProperty("voice",voices[0].id)
        speak(input_text)
        text_box.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid string.")

# Main application window
root = tk.Tk()
root.title("String Converter")
root.geometry("720x480+100+50")  # Fixed size and position
root.resizable(False, False)  # Disable resizing

# Label for instruction
label = tk.Label(root, text="Enter a string (TEXT TO SPEECH):", font=("Arial", 14))
label.pack(pady=20)

# Text box for input
text_box = tk.Entry(root, width=50, font=("Arial", 14))
text_box.pack(pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", font=("Arial", 14), bg="blue", fg="white", command=on_convert)
convert_button.pack(pady=20)

# Bind the Enter key to the on_convert function
root.bind('<Return>', on_convert)

# Run the application
root.mainloop()