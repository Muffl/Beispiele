import numpy as np
import pygame

# Spielkonstanten
CELL_SIZE = 10
WIDTH = 800
HEIGHT = 600
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def nachbar_count(grid, x, y):
    s = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            s += grid[(x + i) % grid.shape[0], (y + j) % grid.shape[1]]
    return s

def update(grid):
    new_grid = grid.copy()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            nachbarn = nachbar_count(grid, x, y)
            if grid[x, y] and (nachbarn < 2 or nachbarn > 3):
                new_grid[x, y] = 0
            elif nachbarn == 3:
                new_grid[x, y] = 1
    return new_grid

def draw_grid(window, grid):
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            if grid[y // CELL_SIZE, x // CELL_SIZE]:
                pygame.draw.rect(window, BLACK, rect)
            else:
                pygame.draw.rect(window, WHITE, rect)
            pygame.draw.line(window, (200, 200, 200), (x, 0), (x, HEIGHT))
            pygame.draw.line(window, (200, 200, 200), (0, y), (WIDTH, y))

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.5, 0.5])
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update(grid)
        draw_grid(window, grid)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
