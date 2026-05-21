# 📝 To-Do List App

A simple and clean task management application built with Python and Gradio UI.

---

## 📌 Project Description

The To-Do List App allows users to manage their daily tasks through a simple graphical interface. Tasks are saved to a JSON file so they persist even after closing the application. Built as part of a B.Sc. Computer Science portfolio project.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.x | Core programming language |
| Gradio | UI framework |
| JSON | Data storage (file handling) |
| OS Module | File path management |
| datetime | Timestamp for tasks |

---

## ✨ Features

- ➕ Add new tasks with timestamp
- ✅ Mark tasks as complete
- 🗑️ Delete individual tasks
- 🧹 Clear all completed tasks at once
- 📊 View task summary (Total / Done / Pending)
- 💾 Tasks saved automatically to `tasks.json`
- 🔄 Data persists across sessions

---

## 📁 Project Structure

```
todo_app/
│
├── todo_app.py       # Main application file
├── tasks.json        # Auto-generated task storage file
└── README.md         # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.7 or above
- pip (Python package manager)

### Step 1 — Clone or Download
```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

### Step 2 — Install Dependencies
```bash
pip install gradio
```

### Step 3 — Run the App
```bash
python todo_app.py
```

### Step 4 — Open in Browser
The app will launch automatically at:
```
http://localhost:7860
```

---

## 🖥️ How to Use

| Action | Steps |
|--------|-------|
| Add Task | Type task name → Click "➕ Add Task" |
| Complete Task | Enter task number → Click "✅ Complete" |
| Delete Task | Enter task number → Click "🗑️ Delete" |
| Clear Completed | Click "🧹 Clear Completed" |
| View Summary | Click "📊 Summary" |

---

## 📸 Screenshots

> Run the app and take a screenshot of the Gradio UI to add here.

---

## 🔮 Future Improvements

- Add due date and priority levels
- Filter tasks by status (All / Pending / Completed)
- Add user login for personal task lists
- Mobile-friendly UI with Gradio themes

---

## 👩‍💻 Author

**Akshaya S**  
B.Sc. Computer Science — Nirmala College for Women, Coimbatore  
📧 achusunil0405@gmail.com

---

## 📄 License

This project is for educational and portfolio purposes.
