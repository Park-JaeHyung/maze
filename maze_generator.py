import random

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    stack = []
    visited = [[False for _ in range(width)] for _ in range(height)]

    def is_valid(ny, nx):
        return 0 <= ny < height and 0 <= nx < width

    def neighbors(y, x):
        dirs = [(0, -2), (-2, 0), (0, 2), (2, 0)]
        result = []
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if is_valid(ny, nx) and not visited[ny][nx]:
                result.append((ny, nx))
        return result

    def carve_passage(y, x):
        visited[y][x] = True
        maze[y][x] = 0
        stack.append((y, x))

        while stack:
            y, x = stack[-1]
            nbs = neighbors(y, x)
            if nbs:
                ny, nx = random.choice(nbs)
                wall_y, wall_x = (y + ny) // 2, (x + nx) // 2
                maze[wall_y][wall_x] = 0
                maze[ny][nx] = 0
                visited[ny][nx] = True
                stack.append((ny, nx))
            else:
                stack.pop()

    carve_passage(1, 1)
    maze[1][1] = 2  # START
    maze[height - 2][width - 2] = 3  # END
    return maze
