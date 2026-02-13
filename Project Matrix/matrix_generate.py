import numpy as np
import random
import time

# Configuration
MATRIX_FILE = "matrix.txt"
ROWS, COLS = 100, 100
CHANGE_RATE = 0.01   # fraction of cells to change per update (e.g. 0.01 = 1%)
INTERVAL = 0.1       # seconds between random updates

def load_matrix(filename):
    """Load a 100x100 matrix from text file, or create one if missing."""
    try:
        mat = np.loadtxt(filename)
        if mat.shape != (ROWS, COLS):
            print(f"Matrix shape mismatch. Recreating new {ROWS}x{COLS} file.")
            mat = np.zeros((ROWS, COLS))
    except Exception:
        print("File not found or invalid. Creating a new one.")
        mat = np.zeros((ROWS, COLS))
    return mat

def save_matrix(filename, mat):
    """Save matrix to text file."""
    np.savetxt(filename, mat, fmt="%.0f")

def random_modify(mat):
    """Randomly change a small number of cells in the matrix."""
    total_changes = int(ROWS * COLS * CHANGE_RATE)
    for _ in range(total_changes):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        mat[r, c] = random.randint(0, 255)
    return mat

def main():
    mat = load_matrix(MATRIX_FILE)
    print("Randomly modifying matrix... (Press Ctrl+C to stop)")
    while True:
        mat = random_modify(mat)
        save_matrix(MATRIX_FILE, mat)
        print("Matrix updated.")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
