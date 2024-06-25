import pygame
pygame.init()

class Game:
    def __init__(self, screenSize):
        self.screenSize=screenSize
        self.run()

    def run(self):
        bgColour="grey"

        screen=pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption("Minesweeper")

        screen.fill(bgColour)

        pygame.display.flip()

        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
