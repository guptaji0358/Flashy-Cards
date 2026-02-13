# Flashy-Cards
DAY - 31 - Project - Python X Flashy Cards
# LinguaFlip – French Flash Cards

A simple desktop flash-card learning app built with **Python** and **Tkinter**.

This project helps users practice French vocabulary by showing a French word first and automatically flipping the card to show the English translation after a short delay.

---

## 📌 Features

* Flash card interface (front & back card design)
* Automatic card flip after 3 seconds
* Random word selection from CSV data
* Mark words as known using ✔ button
* Skip words using ✖ button
* Progress tracking during runtime
* Finish message when all words are learned
* Optional save progress when closing app

---

## 🧱 Tech Used

* Python
* Tkinter (GUI)
* Pandas (CSV handling)
* Random module

---

## 📂 Project Structure

```
LinguaFlip/
│
├── 31_FRENCH_LANGUAGE_FLASH_CARDS.py
├── FRENCH_WORDS.csv
├── CARD_FRONT.png
├── CARD_BACK.png
├── CHECK.png
├── WRONG.png
└── demo.mp4
```

---

## ▶️ How to Run

1. Install requirements:

```
pip install pandas
```

2. Run the project:

```
python 31_FRENCH_LANGUAGE_FLASH_CARDS.py
```

---

## 🎮 How It Works

1. A French word appears on the card.
2. After 3 seconds, the card flips to show English.
3. ✔ = word learned (removed from list).
4. ✖ = skip to next word.
5. When closing, user can choose to save progress.

---

## 📊 Data Source

Words are loaded from:

```
FRENCH_WORDS.csv
```

Each row contains:

```
French | English
```

---

## 🔧 Updates

If you want new features or improvements, view and suggest upgrades — I will upgrade it, and viewers can also upgrade and improve the project.

---

## 🛠️ Error Fix (FileNotFoundError)

If you see this error:

```
FileNotFoundError: [Errno 2] No such file or directory
```

### ✔️ How to Fix

1. Make sure all files are inside the project folder:

```
CARD_FRONT.png
CARD_BACK.png
CHECK.png
WRONG.png
FRENCH_WORDS.csv
```

2. Check file names carefully
   (example: `CARD_FRONT.png` ≠ `card_front.png`).

3. If paths are written like this:

```python
r"E:\some\long\path\file.png"
```

replace them with simple local paths:

```python
"file.png"
```

4. Run the program from the same folder where files exist.

---

If files are in the correct location, the error will be fixed.

---

## 👨‍💻 Author

Robin Gupta

---

## 📜 Project Status

Completed working version.
