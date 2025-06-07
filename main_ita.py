# Name Software: Translate
# Author: Bocaletto Luca
# License: GPLv3
# Language: Italian
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    # Ottieni il testo da tradurre dalla casella di testo di input
    text_to_translate = input_text.get("1.0", "end-1c")
    translator = Translator()

    # Ottieni la lingua di origine e la lingua di destinazione selezionate dall'utente
    src_lang = source_language.get()
    dest_lang = destination_language.get()

    try:
        # Utilizza il traduttore di Google per tradurre il testo
        translated_result = translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
        if translated_result.text is not None:
            # Se la traduzione ha successo, mostra il testo tradotto nell'area di output
            translated_text = translated_result.text
            output_text.config(state="normal")
            output_text.delete("1.0", "end")  # Cancella il campo di output
            output_text.insert("1.0", translated_text)  # Inserisci il testo tradotto
            output_text.config(state="disabled")
        else:
            # Se la traduzione non ha successo, mostra un messaggio di errore nell'area di output
            output_text.config(state="normal")
            output_text.delete("1.0", "end")
            output_text.insert("1.0", "La traduzione non è riuscita. Riprova.")
            output_text.config(state="disabled")
    except Exception as e:
        # Gestisci eventuali eccezioni mostrando un messaggio di errore nell'area di output
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Errore nella traduzione: " + str(e))
        output_text.config(state="disabled")

# Crea la finestra principale
root = tk.Tk()
root.title("Traduttore")

# Crea una casella di testo per l'input
input_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
input_text.grid(row=0, column=0, padx=10, pady=10)

# Crea una casella di testo per l'output (disabilitata inizialmente)
output_text = tk.Text(root, wrap=tk.WORD, width=40, height=10, state="disabled")
output_text.grid(row=0, column=1, padx=10, pady=10)

# Crea le etichette per le lingue
source_language_label = ttk.Label(root, text="Lingua di origine:")
source_language_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
destination_language_label = ttk.Label(root, text="Lingua di destinazione:")
destination_language_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Crea le opzioni per le lingue
languages = ["en", "es", "fr", "de", "it", "ja", "ko", "zh-CN", "ru"]
source_language = ttk.Combobox(root, values=languages)
source_language.grid(row=1, column=1, padx=10, pady=5)
source_language.set("en")  # Imposta la lingua di origine predefinita
destination_language = ttk.Combobox(root, values=languages)
destination_language.grid(row=2, column=1, padx=10, pady=5)
destination_language.set("it")  # Imposta la lingua di destinazione predefinita

# Crea il pulsante di traduzione
translate_button = ttk.Button(root, text="Traduci", command=translate_text)
translate_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Esegui il ciclo principale della GUI
root.mainloop()
