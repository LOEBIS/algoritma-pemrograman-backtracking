import time
import os

N = 4  # ukuran maze

# 1 = jalan, 0 = tembok
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solution = [[0]*N for _ in range(N)]

def print_maze(sol):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(N):
        for j in range(N):
            if sol[i][j] == 1:
                print("🐭", end=" ")
            elif maze[i][j] == 0:
                print("⬛", end=" ")
            else:
                print("⬜", end=" ")
        print()
    time.sleep(0.5)

def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1

def solve_maze(x, y):
    # jika sampai tujuan
    if x == N-1 and y == N-1:
        solution[x][y] = 1
        print_maze(solution)
        return True

    if is_safe(x, y):
        solution[x][y] = 1
        print_maze(solution)

        # gerak kanan
        if solve_maze(x, y+1):
            return True

        # gerak bawah
        if solve_maze(x+1, y):
            return True

        # backtracking (mundur)
        solution[x][y] = 0
        print_maze(solution)
        return False

    return False

# RUN
if solve_maze(0, 0):
    print("\n✅ Jalur ditemukan!")
else:
    print("❌ Tidak ada solusi")
