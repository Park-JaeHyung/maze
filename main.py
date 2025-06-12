import pygame, sys
from maze_generator import generate_maze

pygame.init()
TILE = 20
WIDTH, HEIGHT = 31, 21  # 홀수여야 함
maze = generate_maze(WIDTH, HEIGHT)

SCREEN = pygame.display.set_mode((WIDTH*TILE, HEIGHT*TILE))
pygame.display.set_caption("Maze Game")
CLOCK = pygame.time.Clock()
FONT_LARGE = pygame.font.SysFont(None, 72)
FONT_SMALL = pygame.font.SysFont(None, 36)

player_x, player_y = 1, 1
clear = False

def draw_maze():
    colors = {
        0: (255, 255, 255),  # 통로
        1: (0, 0, 0),        # 벽
        2: (0, 255, 0),      # START
        3: (255, 0, 0)       # END
    }
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = colors.get(maze[y][x], (255, 255, 255))
            pygame.draw.rect(SCREEN, color, (x*TILE, y*TILE, TILE, TILE))

    pygame.draw.circle(SCREEN, (0, 0, 255),
        (player_x*TILE + TILE//2, player_y*TILE + TILE//2), TILE//2)

def handle_movement(keys):
    global player_x, player_y, clear
    dx = dy = 0
    if keys[pygame.K_w]: dy = -1
    if keys[pygame.K_s]: dy = 1
    if keys[pygame.K_a]: dx = -1
    if keys[pygame.K_d]: dx = 1

    nx, ny = player_x + dx, player_y + dy
    if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and maze[ny][nx] != 1:
        player_x, player_y = nx, ny

    if maze[player_y][player_x] == 3:
        clear = True

def show_clear_message():
    msg1 = FONT_LARGE.render("CLEAR!", True, (255, 255, 0))
    msg2 = FONT_SMALL.render("PRESS ESC", True, (200, 200, 200))
    SCREEN.blit(msg1, (WIDTH*TILE//2 - msg1.get_width()//2, HEIGHT*TILE//2 - 60))
    SCREEN.blit(msg2, (WIDTH*TILE//2 - msg2.get_width()//2, HEIGHT*TILE//2 + 10))

while True:
    SCREEN.fill((0, 0, 0))
    draw_maze()

    keys = pygame.key.get_pressed()
    if not clear:
        handle_movement(keys)
    else:
        show_clear_message()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (clear and keys[pygame.K_ESCAPE]):
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    CLOCK.tick(30)
