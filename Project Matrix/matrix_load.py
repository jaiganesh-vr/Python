import tkinter as tk
import numpy as np
import os
import time

# --- Config ---
ROWS, COLS = 100, 100
PIXEL_SIZE = 8
MATRIX_FILE = "matrix.txt"  # text file containing 100x100 numeric values
REFRESH_RATE_MS = 10  # refresh every 0.5 seconds

root = tk.Tk()
root.title("Live 100x100 Grayscale Matrix Viewer")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=COLS * PIXEL_SIZE,
    height=ROWS * PIXEL_SIZE,
    bg="white",
    highlightthickness=0
)
canvas.pack()

# --- Initialize rectangles (like pixels) ---
rects = {}
for r in range(ROWS):
    for c in range(COLS):
        x1, y1 = c * PIXEL_SIZE, r * PIXEL_SIZE
        x2, y2 = x1 + PIXEL_SIZE, y1 + PIXEL_SIZE
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, outline="", fill="#000000")
        rects[(r, c)] = rect_id

# --- Helper function: load matrix from text file ---
def load_matrix(filename):
    """Read 100x100 grayscale values from text file."""
    try:
        data = np.loadtxt(filename)
        if data.shape != (ROWS, COLS):
            print(f"⚠️ Expected shape ({ROWS}, {COLS}), got {data.shape}")
            return None
        return np.clip(data, 0, 255).astype(np.uint8)
    except Exception as e:
        print(f"Error loading matrix: {e}")
        return None

# --- Update grid colors ---
def update_grid(mat):
    for (r, c), rect_id in rects.items():
        v = mat[r, c]
        color = f"#{v:02x}{v:02x}{v:02x}"
        canvas.itemconfig(rect_id, fill=color)

# --- Watch the file for changes ---
last_mtime = 0
def watch_file():
    global last_mtime
    if os.path.exists(MATRIX_FILE):
        mtime = os.path.getmtime(MATRIX_FILE)
        if mtime != last_mtime:
            last_mtime = mtime
            mat = load_matrix(MATRIX_FILE)
            if mat is not None:
                update_grid(mat)
    root.after(REFRESH_RATE_MS, watch_file)

# --- Create default matrix file if missing ---
if not os.path.exists(MATRIX_FILE):
    default_mat = np.linspace(0, 255, COLS)
    matrix = np.tile(default_mat, (ROWS, 1))
    np.savetxt(MATRIX_FILE, matrix, fmt="%.0f")

# --- Load initial data and start watching ---
initial_mat = load_matrix(MATRIX_FILE)
if initial_mat is not None:
    update_grid(initial_mat)

watch_file()
root.mainloop()
