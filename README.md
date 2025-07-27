
# Python Mini-Projects Collection

A collection of small, practical Python projects focusing on various applications like web scraping, data automation, and problem-solving. This repository serves as a showcase of my learning journey and practical skill development in Python.
=======

---

# 🐍 Python Mini-Projects Collection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Termux Friendly](https://img.shields.io/badge/Mobile-Friendly-blueviolet)
![MIT License](https://img.shields.io/badge/License-MIT-green)

A collection of small, practical Python projects focusing on various applications like web scraping, data automation, GUI design, and problem-solving.  
This repository serves as a showcase of my learning journey and practical skill development in Python.

---

## 📚 Table of Contents

- [Project 1: Quotes CLI App](#-quoteapp---python-cli-project)
- [Features](#-features)
- [Usage](#-usage)
- [Output Formats](#output-formats)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Project 2: Quotes App using Kivy](#project-2-quotes-app-using-kivy-mobile-app-gui)
- [Screenshots](#-screenshots)
- [Future Enhancements](#future-enhancements)
- [Learnings](#-learnings)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)
>>>>>>> 397538644717227b352105ec526ef4ee151fcd63

---

## Project 1: Simple Quotes Web Scraper

<<<<<<< HEAD
**Description:**
This project demonstrates basic web scraping capabilities using Python. It will connect to a target website, extract specific textual content (quotes and their authors), and save the collected data into a structured CSV file.

**Problem Solved:**
Automating the collection of specific data from publicly accessible web pages for analysis, archival, or use in other applications.

**Features:**
* Fetches HTML content from `quotes.toscrape.com`.
* Parses the HTML to identify and extract quotes and their corresponding authors.
* Stores the extracted data in a list of dictionaries.
* Exports the collected quotes and authors into a clean CSV file (`quotes.csv`).

**Technologies Used:**
* Python 3.x
* `requests` library (for making HTTP requests)
* `BeautifulSoup4` library (for HTML parsing)
* `csv` module (for CSV file handling)

**How to Run:**
1. Clone this repository: `git clone https://github.com/jit0341/python-mini-projects.git`
2. Navigate to the project directory: `cd python-mini-projects`
3. Install the required libraries: `pip install requests beautifulsoup4`
4. Run the script: `python quotes_scraper.py` (once you create the file)

**Future Enhancements (Planned):**
* Implement pagination to scrape multiple pages.
* Add error handling for network issues or malformed HTML.
* Scrape additional information (e.g., tags for each quote).

---

*(More projects will be added here as I develop them.)*
=======
> A Python-based command-line application to scrape, store, and display quotes with optional filtering.

---

## 💡 Features

- Scrape quotes from the web
- Save quotes to JSON, CSV, and TSV formats
- View or filter quotes from saved files using keywords
- 100+ quotes stored in `quotes_100.json`

---

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

quotes.json



---

🛠️ Project Structure

quotes_app_project/
├── app/
│   └── quote_app.py            # CLI or GUI app
├── assets/
│   └── quotes_100.json         # Final output
├── screenshots/                # App visuals
├── requirements.txt            # pip dependencies
├── .gitignore
└── README.md


---

🧰 Requirements

Python 3.8+

Internet (for scraping)

Termux / Ubuntu (mobile-friendly)

BeautifulSoup

Kivy (for GUI app)



---

⚙️ Installation

git clone https://github.com/jit0341/python-mini-projects.git
cd python-mini-projects
pip install -r requirements.txt


---

Project 2: Quotes App using Kivy (Mobile App GUI)

Description: A mobile app developed with Kivy that displays a random quote and its author each time the user taps a button.
This project is an extension of the web scraping project, turning the scraped data into a simple interactive app.

Problem Solved: Presents data from the quote scraper project in a visual and touch-friendly format for mobile users.


---

✅ Features

Kivy GUI with a clean button and text layout

Loads quotes from a JSON or CSV file

Displays a random quote on button press

Buildable to Android using Buildozer



---

⚙️ Technologies Used

Python 3.x

Kivy

Buildozer (for packaging to Android)



---

📲 Setup

1. Install Kivy (on desktop):



pip install kivy

2. Install Buildozer (on Linux): Follow instructions here


3. Run app locally:



python main.py

4. To build APK:



buildozer init
# Edit buildozer.spec if needed
buildozer -v android debug


---

🧱 Challenges Faced

Setting up Buildozer correctly on Linux

Managing file paths and resources in Android



---

🖼️ Screenshots

CLI App	Kivy App

	


(Add screenshots to the screenshots/ folder)


---

🔮 Future Enhancements

Add swipe gestures to switch quotes

Improve UI with images or backgrounds

Add save/share/favorite functionality

SQLite support for saved quotes

Create Android APK from Kivy GUI app



---

🧠 Learnings

Web scraping using requests and BeautifulSoup

Saving structured data as .json, .csv, .tsv

GUI development using Kivy

Mobile packaging using Buildozer

Using .gitignore to keep repos clean

Structuring Python projects for real use



---

🤝 Contributing

Pull requests are welcome!
If you'd like to add features, fix bugs, or improve documentation, please fork the repository and submit a PR.


---

📌 Author

Made with ❤️ in Termux by Jitendra Bharti


---

🔗 License

MIT License — feel free to use, modify, or share with credit.


---


