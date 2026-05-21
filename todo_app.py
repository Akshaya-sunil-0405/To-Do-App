import gradio as gr
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def format_tasks(tasks):
    if not tasks:
        return "No tasks yet! Add a task to get started."
    lines = []
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "⬜"
        date = task.get("date", "")
        lines.append(f"{status} [{i+1}] {task['title']}  🕒 {date}")
    return "\n".join(lines)

def add_task(title, tasks_state):
    if not title.strip():
        return tasks_state, format_tasks(tasks_state), "⚠️ Task title cannot be empty!"
    task = {
        "title": title.strip(),
        "done": False,
        "date": datetime.now().strftime("%d %b %Y, %I:%M %p")
    }
    tasks_state.append(task)
    save_tasks(tasks_state)
    return tasks_state, format_tasks(tasks_state), f"✅ Task '{title.strip()}' added!"

def complete_task(task_num, tasks_state):
    try:
        idx = int(task_num) - 1
        if idx < 0 or idx >= len(tasks_state):
            return tasks_state, format_tasks(tasks_state), "⚠️ Invalid task number!"
        tasks_state[idx]["done"] = True
        save_tasks(tasks_state)
        return tasks_state, format_tasks(tasks_state), f"🎉 Task {task_num} marked as complete!"
    except ValueError:
        return tasks_state, format_tasks(tasks_state), "⚠️ Please enter a valid number!"

def delete_task(task_num, tasks_state):
    try:
        idx = int(task_num) - 1
        if idx < 0 or idx >= len(tasks_state):
            return tasks_state, format_tasks(tasks_state), "⚠️ Invalid task number!"
        removed = tasks_state.pop(idx)
        save_tasks(tasks_state)
        return tasks_state, format_tasks(tasks_state), f"🗑️ Task '{removed['title']}' deleted!"
    except ValueError:
        return tasks_state, format_tasks(tasks_state), "⚠️ Please enter a valid number!"

def clear_completed(tasks_state):
    tasks_state = [t for t in tasks_state if not t["done"]]
    save_tasks(tasks_state)
    return tasks_state, format_tasks(tasks_state), "🧹 Completed tasks cleared!"

def get_summary(tasks_state):
    total = len(tasks_state)
    done = sum(1 for t in tasks_state if t["done"])
    pending = total - done
    return tasks_state, format_tasks(tasks_state), f"📊 Total: {total} | ✅ Done: {done} | ⏳ Pending: {pending}"

# Load existing tasks on startup
initial_tasks = load_tasks()

with gr.Blocks(title="To-Do List App", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 📝 To-Do List App")
    gr.Markdown("Manage your tasks efficiently — add, complete, and delete tasks with ease.")

    tasks_state = gr.State(initial_tasks)

    with gr.Row():
        with gr.Column(scale=2):
            task_input = gr.Textbox(placeholder="Enter a new task...", label="New Task", lines=1)
            add_btn = gr.Button("➕ Add Task", variant="primary")

        with gr.Column(scale=1):
            task_num_input = gr.Textbox(placeholder="Task number", label="Task Number")
            with gr.Row():
                complete_btn = gr.Button("✅ Complete", variant="secondary")
                delete_btn = gr.Button("🗑️ Delete", variant="stop")

    with gr.Row():
        clear_btn = gr.Button("🧹 Clear Completed")
        summary_btn = gr.Button("📊 Summary")

    task_display = gr.Textbox(
        value=format_tasks(initial_tasks),
        label="Your Tasks",
        lines=12,
        interactive=False
    )
    status_msg = gr.Textbox(label="Status", interactive=False)

    add_btn.click(add_task, [task_input, tasks_state], [tasks_state, task_display, status_msg])
    task_input.submit(add_task, [task_input, tasks_state], [tasks_state, task_display, status_msg])
    complete_btn.click(complete_task, [task_num_input, tasks_state], [tasks_state, task_display, status_msg])
    delete_btn.click(delete_task, [task_num_input, tasks_state], [tasks_state, task_display, status_msg])
    clear_btn.click(clear_completed, [tasks_state], [tasks_state, task_display, status_msg])
    summary_btn.click(get_summary, [tasks_state], [tasks_state, task_display, status_msg])

if __name__ == "__main__":
    app.launch()
