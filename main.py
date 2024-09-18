import pygame

from game.constants import HEIGHT, WIDTH
from game.game_state import GameState
from game.renderer import Renderer


def main():
    """Основная функция игры."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Прототип игры с роботами")

    game_state = GameState()
    renderer = Renderer(screen)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_state.update()
        renderer.draw(game_state)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
