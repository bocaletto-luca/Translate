# Name Software: Translate
# Author: Bocaletto Luca
# License: GPLv3
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    # Get the text to be translated from the input text box
    text_to_translate = input_text.get("1.0", "end-1c")
    translator = Translator()

    # Get the selected source language and destination language from the user
    src_lang = source_language.get()
    dest_lang = destination_language.get()

    try:
        # Use Google Translator to translate the text
        translated_result = translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
        if translated_result.text is not None:
            # If the translation is successful, display the translated text in the output area
            translated_text = translated_result.text
            output_text.config(state="normal")
            output_text.delete("1.0", "end")  # Clear the output field
            output_text.insert("1.0", translated_text)  # Insert the translated text
            output_text.config(state="disabled")
        else:
            # If the translation fails, display an error message in the output area
            output_text.config(state="normal")
            output_text.delete("1.0", "end")
            output_text.insert("1.0", "Translation failed. Please try again.")
            output_text.config(state="disabled")
    except Exception as e:
        # Handle any exceptions by showing an error message in the output area
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Translation error: " + str(e))
        output_text.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Translator")

# Create a text box for input
input_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
input_text.grid(row=0, column=0, padx=10, pady=10)

# Create a text box for output (initially disabled)
output_text = tk.Text(root, wrap=tk.WORD, width=40, height=10, state="disabled")
output_text.grid(row=0, column=1, padx=10, pady=10)

# Create labels for languages
source_language_label = ttk.Label(root, text="Source Language:")
source_language_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
destination_language_label = ttk.Label(root, text="Destination Language:")
destination_language_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Create language options
languages = ["en", "es", "fr", "de", "it", "ja", "ko", "zh-CN", "ru"]
source_language = ttk.Combobox(root, values=languages)
source_language.grid(row=1, column=1, padx=10, pady=5)
source_language.set("en")  # Set the default source language
destination_language = ttk.Combobox(root, values=languages)
destination_language.grid(row=2, column=1, padx=10, pady=5)
destination_language.set("it")  # Set the default destination language

# Create the translation button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the main GUI loop
root.mainloop()
