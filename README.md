# Python Food Billing System

A beginner-friendly Python project featuring both a **Terminal/CLI version** and a **Tkinter GUI version** for ordering fast food and calculating bills with automated discounts.

---

## Features
- **Dual Interface:** Choose between a command-line terminal version (`food_billing.py`) or a desktop graphical interface (`food_billing_gui.py`).
- **Menu Items:**
  1. Pizza — ₹250
  2. Burger — ₹120
  3. Pasta — ₹180
  4. Sandwich — ₹100
- **Automated Discount:** Automatically applies a **10% discount** if the total bill amount is ₹500 or more.
- **Input Validation:** Handles invalid item codes and empty or non-numeric quantities safely.

---

## Project Structure
```text
Python-Food-Billing-System/
│
├── food_billing.py      # Terminal / CLI version using match-case
├── food_billing_gui.py  # Tkinter Desktop GUI version
└── README.md            # Project documentation
