import pygame
import config
pygame.font.init()

h, w = config.height, config.width
GAME_FONT = pygame.font.SysFont('comicsans', 40)

img_size, padding = 128, 16


class ChatModule:
    def __init__(self, png, texts, window):
        img = pygame.image.load(png)
        self.img = pygame.transform.scale(img, (img_size, img_size))
        self.texts = texts

        self.displayChat(window)

    def displayChat(self, window):
        bgc = pygame.Rect(0 + padding, h - img_size - padding, w - padding*2, 130)
        pygame.draw.rect(window, (255, 255, 255), bgc)

        for i in range(len(self.texts)):
            text = GAME_FONT.render(self.texts[i], True, (0, 0, 0))
            window.blit(text, (0 + padding + img_size + padding, h - img_size + padding*2*i))

        window.blit(self.img, (0 + padding, h - img_size - padding))
