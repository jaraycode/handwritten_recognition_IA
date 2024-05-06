import pygame

class window:

    def __init__(self, width = 1000, height = 400, fps = 60) -> None:
        pygame.init()
        pygame.font.init()
        self.timer = pygame.time.Clock()
        self.WIDTH = width
        self.HEIGHT = height
        self.fps = fps
        self.screen = pygame.display.set_mode([self.WIDTH,self.HEIGHT])
        self.font = pygame.font.Font('font/Ubuntu-Regular.ttf',24)
        self.active_color = (255,255,255)
        self.size_brush = 10
        self.painting = []
        self.draw = False

    def cortar(self, img_original):
        return img_original.subsurface(0,0,self.WIDTH,self.HEIGHT)

    def draw_painting(self, screen, color, inicio, fin, radio = 20):
        x = fin[0] - inicio[0]
        y = fin[1] - inicio[1]
        distance = max(abs(x), abs(y))
        for i in range(distance):
            x = int(inicio[0] + float(i) / distance * x)
            y = int(inicio[1] + float(i) / distance * y)
            pygame.draw.circle(screen, color, (x, y), radio)

    def pantalla(self, caption) -> None:
        # Mouse
        #mouse = pygame.mouse.get_pos()
        #left_click = pygame.mouse.get_pressed()[0]

        # Tener su posición y 
        #if mouse[1] < self.HEIGHT-100:
            #pygame.draw.circle(self.screen, self.active_color, mouse, self.size_brush)
        #print(mouse)
        #if left_click and mouse[1] < self.HEIGHT-100:
        #    self.painting.append(('black', mouse, 20))
        #self.draw_painting(painting=self.painting)
        pygame.display.set_caption(caption)
        self.timer.tick(self.fps)
        self.screen.fill('white')
        run = True
        while run:
            #screen.subsurface(0,0,self.WIDTH, self.HEIGHT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] < self.HEIGHT-100:
                if event.button == 1:
                    pygame.draw.circle(self.screen, self.active_color, event.pos, self.size_brush)
                    self.draw = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.draw = False
            elif event.type == pygame.MOUSEMOTION:
                if self.draw and event.pos[0] < self.HEIGHT-100:
                    pygame.draw.circle(self.screen, self.active_color, event.pos, self.size_brush)
                    self.draw_painting(self.screen, self.active_color, event.pos, last, self.size_brush)
                    print(event.pos)
                last = event.pos

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