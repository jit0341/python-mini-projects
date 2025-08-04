import tkinter as tk
import random

# List of quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Every day is a second chance.",
    "Dream big and dare to fail.",
    "Stay positive, work hard, make it happen.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Push yourself, because no one else is going to do it for you.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
]

# Function to show a random quote
def show_quote():
    selected_quote = random.choice(quotes)
    quote_label.config(text=selected_quote)

# Setup GUI window
window = tk.Tk()
window.title("Quote App")
window.geometry("400x200")
window.configure(bg="#f0f0f0")

# Heading
heading = tk.Label(window, text="Motivational Quote", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
heading.pack(pady=10)

# Quote display label
quote_label = tk.Label(window, text="", wraplength=350, justify="center", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
quote_label.pack(pady=20)

# Show Quote button
quote_button = tk.Button(window, text="Show Quote", command=show_quote, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
quote_button.pack()

# Run the app
window.mainloop()