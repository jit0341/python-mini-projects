# Python Mini-Projects Collection

A collection of small, practical Python projects focusing on various applications like web scraping, data automation, and problem-solving. This repository serves as a showcase of my learning journey and practical skill development in Python.

---

## Project 1: Simple Quotes Web Scraper

[... your existing content remains here ...]

---
# 📜 QuoteApp - Python CLI Project

> A Python-based command-line application to scrape, store, and display quotes with optional filtering.

---

## 💡 Features

- Scrape quotes from the web
- Save quotes to JSON, CSV, and TSV formats
- View or filter quotes from saved files using keywords
- 100+ quotes stored in `quotes_100.json`

---

## 🛠️ Project Structure
quote_app.py             # CLI app entry point quote_data_handler.py    # Loads and displays quotes from JSON quotes_scraper.py        # Scrapes quotes from the web scraped_quotes.json      # Original scraped data quotes_100.json          # Cleaned 100+ quotes used in the app

## 🚀 Usage

### 1. Run the App

```bash
python quote_app.py --file quotes_100.json

2. Filter Quotes by Keyword

python quote_app.py --file quotes_100.json --filter life


---

📦 Output Formats

You can convert the JSON quotes to:

quotes.csv
quotes.tsv



---

📁 Archive

Build files and unused configs are moved to the archive/ folder.


---

🧰 Requirements

Python 3.8+

Internet (for scraping)

Termux / Ubuntu (mobile friendly)

📌 Author

Made with ❤️ in Termux by [YourNameHere].


---

🔗 License

MIT License

---

## Project 2: Quotes App using Kivy (Mobile App GUI)

**Description:**
A mobile app developed with Kivy that displays a random quote and its author each time the user taps a button. This project is an extension of the web scraping project, turning the scraped data into a simple interactive app.

**Problem Solved:**
Presents data from the quote scraper project in a visual and touch-friendly format for mobile users.

**Features:**
* Kivy GUI with a clean button and text layout
* Loads quotes from a JSON or CSV file
* Displays a random quote on button press
* Buildable to Android using Buildozer

**Technologies Used:**
* Python 3.x
* Kivy
* Buildozer (for packaging to Android)

**Setup:**
1. Install Kivy (on desktop): `pip install kivy`
2. Install Buildozer (on Linux): Follow instructions [here](https://kivy.org/doc/stable/guide/packaging-android.html)
3. Run app locally: `python main.py`
4. To build APK:
    ```bash
    buildozer init
    # Edit buildozer.spec if needed
    buildozer -v android debug
    ```

**Challenges Faced:**
* Setting up Buildozer correctly on Linux
* Managing file paths and resources in Android

**Future Enhancements:**
* Add swipe gestures to switch quotes
* Improve UI with images/backgrounds
* Add save/share functionality

---

*(More projects will be added here as I develop them.)*
