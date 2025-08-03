import random

quotes = [
    "Believe you can and you're halfway there.",
    "Do something today that your future self will thank you for.",
    "Push yourself, because no one else is going to do it for you.",
    "The only way to do great work is to love what you do.",
    "Stay positive, work hard, make it happen."
]

def show_random_quote():
    print("\n✨ Your Quote for Today:")
    print(random.choice(quotes))

if __name__ == "__main__":
    print("🎯 Welcome to the Quote App (Console Version)")
    input("Press Enter to get a motivational quote... ")
    show_random_quote()
