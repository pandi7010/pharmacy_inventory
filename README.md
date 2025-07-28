# 💊 Pharmacy Inventory System

A lightweight and visually appealing **Pharmacy Inventory System** built entirely in **a single Python Flask file** using **SQLite** for data persistence.  
Ideal for local pharmacies, students, or beginner developers learning Flask and web UI design.

> 🎓 Developed by **Karthiga V – Final year ECE**

---

## 🎯 Features

- 🧾 Add new medicine entries with name, quantity, and price
- 📋 View all inventory in a clean table
- ❌ Delete existing entries with confirmation
- 🎨 Stylish, animated UI using HTML/CSS (no templates folder)
- ⚡️ Everything in **one file** (`pharmacy_inventory.py`)

---

## 🛠 Tech Stack

| Layer      | Technology   |
|------------|--------------|
| Frontend   | HTML, CSS (embedded in Python using `render_template_string`) |
| Backend    | Python (Flask) |
| Database   | SQLite (auto-created on run) |

---

## 📁 File Structure


This file:
- Initializes the SQLite DB (`database.db`)
- Serves the entire app through Flask
- Embeds all HTML, CSS, and logic inside Python

---

## 🚀 How to Run

### 🔧 Step 1: Install Python Dependencies

Make sure Python 3 is installed, then run:

```bash
pip install flask
python pharmacy_inventory.py
