# To-Do List App (Console-based)

A simple command-line to-do list manager built in Python. Tasks are stored persistently in a text file so they survive between runs.

## Features
- View all tasks
- Add a new task
- Remove a task by number
- Tasks persist across sessions using file I/O (`tasks.txt`)

## Tech Stack
- Python 3 (standard library only, no dependencies)

## How to Run

```bash
python todo.py
```

Follow the on-screen menu to view, add, or remove tasks.

## How it Works
- Tasks are stored as plain text, one per line, in `tasks.txt`.
- On startup, the app loads existing tasks from the file.
- Any add/remove operation immediately saves the updated list back to the file.

## Project Structure
```
todo-list-app/
├── todo.py       # Main application
├── tasks.txt     # Auto-created on first run, stores tasks
└── README.md
```
