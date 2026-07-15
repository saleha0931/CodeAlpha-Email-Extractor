"""
Project : Email Address Extractor

Internship : CodeAlpha Python Programming

Developed By: Saleha Shahid

University of Management and Technology
--------------------------------------------------
Scans a text file, finds all email addresses using a regex
pattern, removes duplicates, and saves them to a new file.

Key concepts used: re, os, file handling.

Run:  python extract_emails.py
"""

import os
import re
from datetime import datetime

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class _NoColor:
        def __getattr__(self, name):
            return ""
    Fore = _NoColor()
    Style = _NoColor()


EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


# ------------------------------------------------------------
# UI helpers
# ------------------------------------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def box(title, width=58, color=Fore.CYAN):
    print(color + "╔" + "═" * (width - 2) + "╗")
    print(color + "║" + title.center(width - 2) + "║")
    print(color + "╚" + "═" * (width - 2) + "╝" + Style.RESET_ALL)


def divider(width=58, char="─", color=Fore.LIGHTBLACK_EX):
    print(color + char * width + Style.RESET_ALL)


def success(msg):
    print(Fore.GREEN + "✔  " + msg + Style.RESET_ALL)


def warn(msg):
    print(Fore.YELLOW + "⚠  " + msg + Style.RESET_ALL)


def error(msg):
    print(Fore.RED + "✘  " + msg + Style.RESET_ALL)


def info(msg):
    print(Fore.CYAN + "ℹ  " + msg + Style.RESET_ALL)


def show_welcome_screen():
    clear_screen()
    art = r"""
    ______           _ __
   / ____/___ ___  ____ _(_) /
  / __/ / __ `__ \/ __ `/ / /
 / /___/ / / / / / /_/ / / /
/_____/_/ /_/ /_/\__,_/_/_/

  E M A I L   E X T R A C T O R
"""
    print(Fore.MAGENTA + Style.BRIGHT + art + Style.RESET_ALL)
    box("Welcome! 📧", color=Fore.CYAN)
    print(Fore.WHITE + """
  Point this at any .txt file and it will pull out every
  email address it finds, remove duplicates, and save a
  clean list to a new file.
""" + Style.RESET_ALL)
    divider()
    input(Fore.GREEN + "\n  Press Enter to continue..." + Style.RESET_ALL)


# ------------------------------------------------------------
# Core logic
# ------------------------------------------------------------
def extract_emails():
    box("EXTRACT EMAIL ADDRESSES", color=Fore.CYAN)
    source = input("\nPath to the .txt file to scan: ").strip('"').strip()

    if not os.path.isfile(source):
        error(f"'{source}' is not a valid file.")
        return

    try:
        with open(source, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except IOError as e:
        error(f"Could not read the file: {e}")
        return

    emails = sorted(set(EMAIL_PATTERN.findall(content)))

    if not emails:
        warn("No email addresses found in that file.")
        return

    print(f"\n{Fore.GREEN}Found {len(emails)} unique email address(es):{Style.RESET_ALL}")
    divider()
    for e in emails:
        print(f"  • {e}")
    divider()

    default_out = os.path.join(os.path.dirname(source) or ".", "extracted_emails.txt")
    out_path = input(f"\nSave to (Enter for '{default_out}'): ").strip('"').strip()
    out_path = out_path or default_out

    with open(out_path, "w") as f:
        f.write(f"Extracted from: {source}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total found: {len(emails)}\n")
        f.write("-" * 40 + "\n")
        f.write("\n".join(emails))

    success(f"Saved {len(emails)} email(s) to: {out_path}")


def main():
    show_welcome_screen()

    while True:
        extract_emails()
        again = input(Fore.YELLOW + "\nScan another file? (y/n): "
                       + Style.RESET_ALL).strip().lower()
        if again != "y":
            print(Fore.MAGENTA + "\nThanks for using the Email Extractor! 📧\n"
                  + Style.RESET_ALL)
            break
        clear_screen()


if __name__ == "__main__":
    main()
