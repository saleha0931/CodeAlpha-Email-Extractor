# 📧 Email Extractor

A Python automation script developed as part of the **CodeAlpha Python Programming Internship** (Task 3: Task Automation with Python Scripts).

This tool scans any `.txt` file, automatically detects and extracts all valid email addresses using regular expressions, removes duplicates, and saves a clean list to a new output file — a common real-life automation task for handling reports, contact lists, or scraped text data.

---

## ✨ Features

- 📂 Scans any `.txt` file for email addresses
- 🔍 Uses regex pattern matching to reliably detect valid email formats
- 🧹 Automatically removes duplicate emails
- 🔤 Sorts results alphabetically
- 💾 Saves extracted emails to a new `.txt` file, with date and total count
- 🔁 Option to scan multiple files in one session
- 🎨 Optional colored terminal interface (works without Colorama as well)
- ✅ Input validation and friendly error messages

---

## 🛠️ Technologies Used

- Python 3
- `re` (Regular Expressions)
- `os` Module
- `datetime`
- Colorama (Optional)

---

## 📂 Project Structure

```text
CodeAlpha_EmailExtractor/
│── email extractor.py
│── README.md
```

> Output files (e.g. `extracted_emails.txt`) are generated automatically each time you run the script and are not part of the repository.

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python "email extractor.py"
```

> Note: since the filename contains a space, it must be wrapped in quotes when running it from the terminal.

5. When prompted, enter the path to the `.txt` file you want to scan (e.g. `sample.txt` if it's in the same folder, or a full path like `C:\Users\dell\Downloads\emails.txt`).

**Optional:** Install Colorama for a colored terminal interface.

```bash
pip install colorama
```

The application also works correctly without Colorama (plain text mode).

---

## 🎯 Learning Outcomes

This project demonstrates the use of:

- Regular Expressions (`re` module)
- File Handling (reading and writing `.txt` files)
- Set Operations (removing duplicates)
- Exception Handling
- Modular Programming
- User Input Validation

---

## 👩‍💻 Developed By

**Saleha Shahid**
BS Electrical Engineering
University of Management and Technology (UMT)

---

## 📌 Internship

CodeAlpha – Python Programming Internship
