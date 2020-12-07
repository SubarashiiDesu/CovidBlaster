import sys

import menus
from player import Player
from sprite import Sprite
from platforms import Platform
from window_settings import *


class GameState:
    def __init__(self):
        self.name = ""
        self.player = None
        self.difficulty = 3
        self.score = 0
        self.game_over = False
        self.sprites = pygame.sprite.OrderedUpdates()
        self.platforms = pygame.sprite.Group()

    def init_platforms(self):
        temp = []
        h = PY(0.08)
        temp.append(Platform(0, PY(0.85), WIDTH, h))
        temp.append(Platform(PX(0.425), PY(0.45), PX(0.15), h))
        temp.append(Platform(0, PY(0.2), PX(0.33), h))
        temp.append(Platform(PX(0.67), PY(0.2), PX(0.33), h))
        for i in range(0, len(temp)):
            self.platforms.add(temp[i])

    def on_platform(self, player):
        for platform in self.platforms:
            coll = pygame.sprite.collide_rect(platform, player)
            if coll:
                return True
        return False

    def set_name(self, name):
        menus.SOUND.play_event()
        self.name = name.upper()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_player(self, pcolor):
        idle = Sprite(pcolor + "idle.png", 5, upscale=2)
        run = Sprite(pcolor + "run.png", 6, upscale=2)
        jump = Sprite(pcolor + "jump.png", 2, upscale=2)
        crouch = Sprite(pcolor + "crouch.png", 3, upscale=2)
        death = Sprite(pcolor + "death.png", 8, upscale=2)
        ps = {"idle": idle, "run": run, "jump": jump, "crouch": crouch, "death": death}
        self.player = Player(ps, self.difficulty)

    def set_score(self, score):
        self.score = score
