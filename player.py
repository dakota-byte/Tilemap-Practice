import pygame
import os

player_img = pygame.image.load(os.path.join('Assets', 'ditto.png'))
player_img = pygame.transform.rotate(
    pygame.transform.scale(player_img, (32, 32)), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = player_img.convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 6
        self.bounds = []
        self.ibounds = []

    def setPos(self, loc):
        self.rect.x = loc[0]
        self.rect.y = loc[1]

    def interact(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            for ibound in self.ibounds:
                if ibound[0].colliderect(self.rect):
                    # print("interactive type: ", ibound[1])
                    return ibound[1]
        return -1

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            if self.canWalk(self.rect.x + self.speed, self.rect.y):
                self.rect.x += self.speed
        if keys[pygame.K_a]:
            if self.canWalk(self.rect.x - self.speed, self.rect.y):
                self.rect.x -= self.speed
        if keys[pygame.K_w]:
            if self.canWalk(self.rect.x, self.rect.y - self.speed):
                self.rect.y -= self.speed
        if keys[pygame.K_s]:
            if self.canWalk(self.rect.x, self.rect.y + self.speed):
                self.rect.y += self.speed

    def get_map_input(self, slx, sly):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.canWalk(self.rect.x + self.speed, self.rect.y):
                slx -= self.speed
        if keys[pygame.K_LEFT]:
            if self.canWalk(self.rect.x - self.speed, self.rect.y):
                slx += self.speed
        if keys[pygame.K_UP]:
            if self.canWalk(self.rect.x, self.rect.y - self.speed):
                sly += self.speed
        if keys[pygame.K_DOWN]:
            if self.canWalk(self.rect.x, self.rect.y + self.speed):
                sly -= self.speed

        return slx, sly

    def cleariBounds(self):
        self.ibounds = []

    def setiBounds(self, boundrects, boundtypes):
        for i in range(len(boundrects)):
            iboundRectType = [boundrects[i], boundtypes[i]]
            self.ibounds.append(iboundRectType)

    def clearBounds(self):
        self.bounds = []

    def setBounds(self, boundrects):
        for bound in boundrects:
            self.bounds.append(bound)

    def canWalk(self, x, y):
        for bound in self.bounds:
            if bound.collidepoint(x, y):
                return False
            if bound.collidepoint(x + self.rect.width, y):
                return False
            if bound.collidepoint(x, y + self.rect.height):
                return False
            if bound.collidepoint(x + self.rect.width, y + self.rect.height):
                return False
        return True

    def update(self):
        self.get_input()
