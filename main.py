import pygame
import sys
from player import Player
from ChatModule import ChatModule
import sprite_config
import config

PLAYER_DEFAULT_SCREEN_POS = (config.width / 2 - 20, config.height / 2 - 50)


def handleInteraction(interact):
    scene = game.currentScene.getName()

    if interact == -1:
        return

    if scene == "shop":
        if interact == 0:
            # skelly chat
            ChatModule("Assets/PNG/skelly.png", ["who let you in?", "we aren't open"], WINDOW)

        if interact == 1:
            # door, shop -> outside
            game.currentScene = sprite_config.outside_scene
            game.screen_locx = sprite_config.outside_scene_loc[0]
            game.screen_locy = sprite_config.outside_scene_loc[1]
            game.player_obj.setPos(PLAYER_DEFAULT_SCREEN_POS)

    # doesnt exist for now
    if scene == "test":
        if interact == 1:
            # door, test -> shop
            game.currentScene = sprite_config.shop_scene
            game.screen_locx = sprite_config.shop_scene_loc[0]
            game.screen_locy = sprite_config.shop_scene_loc[1]
            game.player_obj.setPos(PLAYER_DEFAULT_SCREEN_POS)

    if scene == "outside":
        if interact == 0:
            # door, outside -> shop
            game.currentScene = sprite_config.shop_scene
            game.screen_locx = sprite_config.shop_scene_loc[0]
            game.screen_locy = sprite_config.shop_scene_loc[1]
            game.player_obj.setPos(PLAYER_DEFAULT_SCREEN_POS)

        if interact == 1:
            ChatModule("Assets/PNG/sign.png", ["WARNING:", "DO NOT CROSS BRIDGE"], WINDOW)


class Game:
    def __init__(self):
        # Screen setup
        self.screen_locx = sprite_config.outside_scene_loc[0]
        self.screen_locy = sprite_config.outside_scene_loc[1]

        self.currentScene = sprite_config.outside_scene

        # Player setup
        self.player_obj = Player(PLAYER_DEFAULT_SCREEN_POS)  # Position (x,y)
        self.player = pygame.sprite.GroupSingle(self.player_obj)

    def run(self):
        # Fill WINDOW
        WINDOW.fill((30, 30, 30))

        # Change x,y depending on Arrow Key Movement
        self.screen_locx, self.screen_locy = self.player_obj.get_map_input(self.screen_locx, self.screen_locy)

        # Setting map bounds
        self.player_obj.clearBounds()
        sceneBoundRects = self.currentScene.getAllBounds(self.screen_locx, self.screen_locy)
        self.player_obj.setBounds(sceneBoundRects)

        # Drawing our map
        self.currentScene.drawEntireScene(WINDOW, self.screen_locx, self.screen_locy)

        # Setting map ibounds
        if self.currentScene.containsInteractive():
            self.player_obj.cleariBounds()
            sceneiBoundRects, sceneiBoundTypes = self.currentScene.getAlliBounds(self.screen_locx, self.screen_locy)
            self.player_obj.setiBounds(sceneiBoundRects, sceneiBoundTypes)
            # Handle player Interaction
            interactionType = self.player_obj.interact()
            handleInteraction(interactionType)

        # Updating player
        self.player.update()
        self.player.draw(WINDOW)


if __name__ == '__main__':
    pygame.init()
    screen_width = config.width
    screen_height = config.height
    WINDOW = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("tilemap practice")
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run()
        pygame.display.flip()
        clock.tick(60)
