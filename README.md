# 🐍 Python Assignments by Sir Zia

This repository contains Python assignments and mini-projects given by **Sir Zia Khan** as part of the **GIAIC curriculum**. It includes core Object-Oriented Programming (OOP) concepts, additional challenges, and hands-on mini-projects for practical learning.

---

## 📚 Topics Covered

### 🔸 Object-Oriented Programming (OOP)
- Classes and Objects
- Instance, Class, and Static Variables/Methods
- Constructors and Destructors
- Access Modifiers (Public, Protected, Private)
- Inheritance and `super()`
- Abstract Classes (`abc` module)
- `@property`, Setter, and Deleter
- Class and Function Decorators
- Method Resolution Order (MRO) and Diamond Inheritance
- Iterators and `__call__()` usage
- Custom Exceptions

---

## 🚀 Additional Challenges

### 🔹 Data Persistence
- Store encrypted data in a JSON file instead of memory.
- Load encrypted data on app startup for continuity.

### 🔹 Advanced Security Features
- Time-based lockout for failed login attempts.
- PBKDF2 hashing for secure password storage.
- Multi-user authentication with Streamlit interface.

---

## 🧩 Mini Projects

### 📘 1. Personal Library Manager (CLI)
- Add/remove/search books with attributes like title, author, year, and genre.
- Statistics for total/read books.
- File handling to save/load book records.

### 🔐 2. Password Strength Meter
- Checks password strength using rules for length and character variety.
- Categorizes as Weak, Moderate, or Strong.
- Gives improvement tips.

### 🔄 3. Google Unit Converter (Streamlit)
- A beautiful and simple **unit conversion app** like Google’s converter.
- Built using **Streamlit** and **Python**.
- Converts between:
  - Length (meters, km, miles)
  - Weight (kg, pounds)
  - Temperature (°C, °F)
  - Time (seconds, minutes, hours)
- User-friendly interface with dropdowns and instant results.

> Run with:
```bash
streamlit run unit_converter.py
