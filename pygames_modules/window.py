import pygame

class window:

    def __init__(self, width = 500, height = 300, fps = 60) -> None:
        self.timer = pygame.time.Clock()
        self.WIDTH = width
        self.HEIGHT = height
        self.fps = fps

    def pantalla(self, caption) -> None:
        screen = pygame.display.set_mode([self.WIDTH,self.HEIGHT])
        pygame.display.set_caption(caption)
        run = True
        while run:
            self.timer.tick(self.fps)
            screen.fill('white')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    prueba = window()
    prueba.pantalla('Handwritten text')