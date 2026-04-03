# 📂 File Organizer (Advanced CLI Tool)

## 📌 Description

A powerful Python-based file organizer that automatically sorts files into categorized folders.
It supports **custom categories**, **date-based sorting**, and an **interactive command-line interface** for a professional user experience.

---

## 🚀 Features

* 📁 Organize files by type (Images, Videos, Documents, etc.)
* 🧠 Custom categories (user-defined folders with extensions)
* 📅 Optional date-based sorting (e.g., `Images/2024/`)
* ⚡ Fast and automated file management
* 🖥️ Interactive CLI with guided user input
* 🛡️ Error handling to prevent crashes
* 📊 Clean summary output after execution

---

## 🛠️ Technologies Used

* Python
* `os` module (file handling)
* `shutil` module (file movement)
* `datetime` module (date sorting)

---

## 📁 How It Works

1. User selects a source folder
2. Optionally selects a destination folder
3. Chooses sorting mode:

   * By type
   * By type + date
4. Optionally adds custom categories
5. Script automatically organizes files into structured folders

---

## 🧩 Example Output

### 👉 Option 1: Organize by Type

```
Images/
Videos/
Documents/
```

### 👉 Option 2: Organize by Type + Date

```
Images/
   2024/
   2025/

Videos/
   2023/
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/Satnamsingh144/file-organizer.git
```

2. Navigate to the project folder:

```
cd file-organizer
```

3. Run the script:

```
python main.py
```

---

## ⚙️ Custom Categories Example

You can define your own folders:

```
Notes → pdf, txt
Photos → jpg, png
```

Output:

```
Notes/
Photos/
```

---

## 📊 Sample Output

```
===== FILE SUMMARY =====
Images      : 10
Videos      : 5
Documents   : 3
------------------------
Total files : 18

✔ Files organized successfully!
```

---

## 🔮 Future Improvements

* 🖥️ GUI version (desktop app)
* 📦 Convert to executable (.exe)
* ☁️ Cloud storage integration
* 🧾 Logging system for file tracking

---

## 👨‍💻 Author

Satnam Singh

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub!

