import tkinter as tk
from tkinter import messagebox


def calculate_bill():
  try:
    # Get selected item from listbox or radio buttons
    selected = item_var.get()
    qty_str = qty_entry.get().strip()

    if not qty_str:
      messagebox.showerror("Error", "Please enter quantity!")
      return

    qty = int(qty_str)
    if qty <= 0:
      messagebox.showerror("Error", "Quantity must be greater than 0!")
      return

    # Price mapping based on selection
    prices = {1: 250, 2: 120, 3: 180, 4: 100}

    if selected not in prices:
      messagebox.showerror("Error", "Please select a valid menu item!")
      return

    price = prices[selected]
    total = price * qty
    discount_applied = False

    # Apply 10% discount if total >= 500
    if total >= 500:
      total = total - (total * 10 / 100)
      discount_applied = True

    # Display result
    result_text = f"Item Price: ₹{price}\nQuantity: {qty}\n"
    if discount_applied:
      result_text += "Discount: 10% applied!\n"
    result_text += f"Total Bill: ₹{total:.2f}"

    result_label.config(text=result_text, fg="green")

  except ValueError:
    messagebox.showerror("Error", "Please enter a valid numeric quantity!")


# Create main window
root = tk.Tk()
root.title("Food Billing System")
root.geometry("350x400")
root.config(bg="#f4f4f4")

# Title Label
title_label = tk.Label(
    root,
    text="Fast Food Billing",
    font=("Arial", 16, "bold"),
    bg="#f4f4f4",
    fg="#333",
)
title_label.pack(pady=15)

# Menu Frame
menu_frame = tk.LabelFrame(
    root, text=" Menu ", font=("Arial", 11, "bold"), bg="#f4f4f4", padx=10, pady=10
)
menu_frame.pack(fill="x", padx=20)

item_var = tk.IntVar(value=0)

menu_items = [("1. Pizza - ₹250", 1), ("2. Burger - ₹120", 2), ("3. Pasta - ₹180", 3), ("4. Sandwich - ₹100", 4)]

for text, val in menu_items:
  tk.Radiobutton(
      menu_frame,
      text=text,
      variable=item_var,
      value=val,
      bg="#f4f4f4",
      font=("Arial", 10),
  ).pack(anchor="w", pady=2)

# Quantity Frame
qty_frame = tk.Frame(root, bg="#f4f4f4")
qty_frame.pack(fill="x", padx=20, pady=15)

tk.Label(
    qty_frame, text="Quantity:", font=("Arial", 10), bg="#f4f4f4"
).pack(side="left")
qty_entry = tk.Entry(qty_frame, font=("Arial", 10), width=10)
qty_entry.pack(side="right")

# Calculate Button
calc_btn = tk.Button(
    root,
    text="Calculate Bill",
    font=("Arial", 11, "bold"),
    bg="#28a745",
    fg="white",
    command=calculate_bill,
)
calc_btn.pack(pady=5)

# Result Label
result_label = tk.Label(
    root, text="", font=("Arial", 11, "bold"), bg="#f4f4f4", justify="left"
)
result_label.pack(pady=15)

# Run application
root.mainloop()