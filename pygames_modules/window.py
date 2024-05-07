import pygame
from predict import Predict

class window:

    def __init__(self, width = 1000, height = 400, fps = 120) -> None:
        pygame.init()
        pygame.font.init()
        self.timer = pygame.time.Clock()
        self.WIDTH = width
        self.HEIGHT = height
        self.fps = fps
        self.screen = pygame.display.set_mode([self.WIDTH,self.HEIGHT])
        self.font = pygame.font.Font('font/Ubuntu-Regular.ttf',24)
        self.active_color = (0,0,0)
        self.size_brush = 10
        self.painting = []
        self.draw = False

    def cut_image(self, img_original):
        return img_original.subsurface(0,0,self.WIDTH,self.HEIGHT-100)

    def draw_painting(self, painting):
        for i in range(len(painting)):
            pygame.draw.circle(self.screen, painting[i][0], painting[i][1], painting[i][2])

    def clean_board(self):
        self.painting = []
        self.screen.fill('white')

    def predict(self):
        model = Predict()
        pass

    def pantalla(self, caption) -> None:        
        pygame.display.set_caption(caption)
        run = True
        while run:
            self.timer.tick(self.fps)
            self.screen.fill('white')
            #screen.subsurface(0,0,self.WIDTH, self.HEIGHT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            # Mouse
            mouse = pygame.mouse.get_pos()
            left_click = pygame.mouse.get_pressed()[0]

            # Tener su posición y pintar en la ubicación deseada 
            if mouse[1] < self.HEIGHT-100:
                pygame.draw.circle(self.screen, self.active_color, mouse, self.size_brush)

            if left_click and mouse[1] < self.HEIGHT-100:
                self.painting.append((self.active_color, mouse, self.size_brush))

            self.draw_painting(painting=self.painting)

            if left_click and mouse[1] > self.HEIGHT-75 and mouse[1] < self.HEIGHT-25 and mouse[0] > self.WIDTH-900 and mouse[0] < self.WIDTH-750:
                pygame.image.save(self.cut_image(self.screen), "word.jpg")
                print("Boton predecir")
            elif left_click and mouse[1] > self.HEIGHT-75 and mouse[1] < self.HEIGHT-25 and mouse[0] > self.WIDTH-700 and mouse[0] < self.WIDTH-550:
                self.clean_board() # Limpia la pantalla

            #if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] < self.HEIGHT-100:
            #    if event.button == 1:
            #        pygame.draw.circle(self.screen, self.active_color, event.pos, self.size_brush)
            #        self.draw = True
            #elif event.type == pygame.MOUSEBUTTONUP:
            #   self.draw = False
            #elif event.type == pygame.MOUSEMOTION:
            #    if self.draw and event.pos[0] < self.HEIGHT-100:
            #        pygame.draw.circle(self.screen, self.active_color, event.pos, self.size_brush)
            #        self.draw_painting2(self.screen, self.active_color, event.pos, last, self.size_brush)
            #        print(event.pos)
            #    last = event.pos

            # Barra inferior
            pygame.draw.rect(self.screen, 'pink', (0,self.HEIGHT-100, self.WIDTH, self.HEIGHT-300))
            # Linea divisoria
            pygame.draw.rect(self.screen, 'gray', (0,self.HEIGHT-100, self.WIDTH, self.HEIGHT-395))
            # Mostrar botones
            pygame.draw.rect(self.screen, 'gray',(self.WIDTH-900, self.HEIGHT-75, 150,50))
            pygame.draw.rect(self.screen, 'gray',(self.WIDTH-700, self.HEIGHT-75, 150,50))
            text = self.font.render("Predecir", True, 'white')
            self.screen.blit(text, (self.WIDTH-875, self.HEIGHT-65))
            text = self.font.render("Limpiar", True, 'white')
            self.screen.blit(text, (self.WIDTH-675, self.HEIGHT-65))
            # Mostrar en pantalla
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    prueba = window()
    prueba.pantalla('Handwritten text')