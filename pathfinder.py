import curses
from curses import wrapper
import queue
import time

# Constants should be uppercase
MAZE = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze: list[list[str]], stdscr: curses.window, path: list[tuple[int, int]] | None = None) -> None:
    """Draws the maze and the current search path on the terminal screen."""
    if path is None:
        path = []

    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                # Multiply j by 2 to add horizontal spacing and make the maze look like a square
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)

def find_start(maze: list[list[str]], start: str) -> tuple[int, int] | None:
    """Iterates through the grid to find the starting coordinates."""
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_neighbors(maze: list[list[str]], row: int, col: int) -> list[tuple[int, int]]:
    """Checks adjacent cells (Up, Down, Left, Right) to see if they are valid moves."""
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors

def find_path(maze: list[list[str]], stdscr: curses.window) -> list[tuple[int, int]] | None:
    """Executes a Breadth-First Search (BFS) to find the shortest path from 'O' to 'X'."""
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    if not start_pos:
        return None

    # Queue stores tuples of: (current_position, path_taken_to_get_here)
    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()
    visited.add(start_pos) # Prevent the algorithm from re-visiting the starting node

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        # Update the UI
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        # Check if we reached the end
        if maze[row][col] == end:
            return path

        # Add valid, unvisited neighbors to the queue
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
            
    return None # Returns None if no path is mathematically possible

def main(stdscr: curses.window) -> None:
    """Main execution block."""
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(MAZE, stdscr)
    
    # Let the user view the final result until they press a key
    stdscr.addstr(len(MAZE) + 1, 0, "Path found! Press any key to exit.")
    stdscr.getch()

if __name__ == "__main__":
    wrapper(main)