import pygame.display
from levels import level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10
from objects import *
from tools.colors import *

pygame.init()
resolution = (1280, 720)
window = pygame.display.set_mode(resolution)


class Game:
    def __init__(self, player):
        self.levels = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10]
        self.current_level = None

        self.serca = None
        self.camera = None
        self.player = player
        self.door = None
        self.ghosts = None
        self.coins = None
        self.beams2 = None
        self.beams = None

        self.label_score = Text(970, 10)
        self.score = 0

        self.skins = {"John": {"acquired": True, "price": 0}, "Jan": {"acquired": False, "price": 100}}
        self.active_skin = "John"

    def load_level(self, level: dict):
        self.current_level = level["nb_level"]
        self.beams = level['beams']
        self.beams2 = level['beams2']
        self.coins = level['coins']
        self.ghosts = level['ghosts']
        self.door = level['door']
        self.camera = level['background']
        self.serca = level['serce']  # hearts

        if "spawn" in level:
            print("Loading spawn")
            self.player.x_cord = level["spawn"][0]
            self.player.y_cord = level["spawn"][1]
        else:
            print("No spawn found")
            self.player.x_cord = 0
            self.player.y_cord = 0

    def run(self):
        run = True
        pause = False

        clock = pygame.time.Clock()

        print(f"Player pos : {self.player.x_cord}, {self.player.y_cord}")
        while run:
            delta = clock.tick(60)

            print(f"FPS: {clock.get_fps():.1f}", end="\r")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    pause = not pause
            self.update(delta)
            self.draw()
            pygame.display.update()

            if not self.player.alive:
                run = False
                self.player.ver_velocity = 0

        self.menu(self.current_level)

    def update(self, delta):
        keys = pygame.key.get_pressed()
        self.camera.tick(self.player)
        self.player.tick(keys, self.beams, self.beams2, delta)
        for ghost in self.ghosts:
            ghost.tick(self.beams, self.beams2, self.player, ghost.start_x - 120, ghost.start_x + 120, delta)
        for coin in self.coins:
            coin.tick()
        for beam2 in self.beams2:
            beam2.tick(self.player)
        for coin in self.coins:
            if coin.hitbox.colliderect(self.player.hitbox):
                self.coins.remove(coin)
                self.score += 100
        for serce in self.serca:
            if serce.hitbox.colliderect(self.player.hitbox) and self.player.health < 100:
                self.serca.remove(serce)
                self.player.health += 10

        if self.player.y_cord > 2000:
            self.player.alive = False

        # check win
        if self.door.hitbox.colliderect(self.player.hitbox):
            self.go_to_next_level()

    def draw(self):
        self.camera.draw(window)

        for beam in self.beams:
            beam.draw(window, self.camera)

        for beam2 in self.beams2:
            beam2.draw(window, self.camera)

        self.player.draw(window, self.camera)

        if self.door:
            self.door.draw(window, self.camera)

        for e in self.coins + self.serca + self.ghosts:
            e.draw(window, self.camera)
        self.label_score.draw(window, self.score)

    def go_to_next_level(self):
        self.player.x_cord = 0
        self.player.y_cord = 0
        if self.current_level < len(self.levels):
            self.load_level(self.levels[self.current_level]())
        else:
            print("You win!")
            pygame.quit()

    def menu(self, current_level):
        run = True
        clock = pygame.time.Clock()
        background = pygame.image.load('Sprites/main menu/menu_background.png').convert_alpha()

        # reset player if it died
        if not self.player.alive:
            self.player.health = 100
            self.player.alive = True

        play_button = Button(515, 500, "Sprites/next_level/next")
        shop_button = Button(900, 500, "Sprites/next_level/next")
        level_menu_button = Button(100, 500, "Sprites/next_level/next")

        font = pygame.font.SysFont('None', 100)
        text = font.render('Game Over', True, RED)
        while run:
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            if play_button.tick():
                run = False
                self.load_level(self.levels[current_level - 1]())
                self.run()
                return

            if level_menu_button.tick():
                self.level_selection()
                return

            if shop_button.tick():
                self.shop()

            window.blit(background, (0, 0))
            window.blit(text, (400, 300))
            play_button.draw(window)
            shop_button.draw(window)
            level_menu_button.draw(window)

            pygame.display.flip()

    def level_selection(self):
        n = len(self.levels)
        run = True
        clock = pygame.time.Clock()
        background = pygame.image.load('Sprites/main menu/menu_background.png').convert_alpha()

        level_buttons = []
        for i in range(n):
            btn = ButtonLevelMenu(170 + 200 * (i % 5), 400 + 150 * (i // 5), f"{i + 1}")
            level_buttons.append(btn)

        while run:
            clock.tick(60)  # maksymalnie 60 fps
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                    pygame.quit()

            for btn in level_buttons:
                btn.update()

            for i in range(n):
                if level_buttons[i].tick(events):
                    level = i + 1
                    self.load_level(self.levels[level - 1]())
                    self.run()

            window.blit(background, (0, 0))

            # draw title
            font = pygame.font.SysFont('None', 100)
            title = font.render("Chose your level : ", True, (230, 225, 240))
            window.blit(title, (50, 300))
            for btn in level_buttons:
                btn.draw(window)

            pygame.display.update()

    def shop(self):
        run = True
        text = Text(950, 10)
        background = pygame.image.load('Sprites/main menu/menu_background.png')

        current_index = 0
        available_skins = list(self.skins.keys())
        current_skin = available_skins[current_index]

        skin_imgs = [pygame.image.load(f"Sprites/characters/{skin}/stand.png").convert_alpha() for skin in
                     available_skins]

        btn_goback = ButtonImg(20, 200, "Sprites/buttons/back")
        btn_left = ButtonImg(200, 400, "Sprites/strzalka")
        btn_right = ButtonImg(1000, 400, "Sprites/strzalkapr")
        btn_buy = ButtonLevelMenu(700, 600, "BUY")
        btn_equip = ButtonLevelMenu(420, 600, "ACTIVATE", width=200)

        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            if btn_left.tick(events):
                current_index = (current_index - 1) % len(available_skins)
                current_skin = available_skins[current_index]
            if btn_right.tick(events):
                current_index = (current_index + 1) % len(available_skins)
                current_skin = available_skins[current_index]
            if btn_buy.tick(events) and not self.skins[current_skin]["acquired"]:
                price = self.skins[current_skin]["price"]
                if self.score >= price:
                    print("bought")
                    self.score -= price
                    self.skins[current_skin]["acquired"] = True

            if btn_equip.tick(events):
                if self.skins[current_skin]["acquired"] and current_skin != self.active_skin:
                    print("equipped")
                    self.active_skin = current_skin
                    self.player.load_skin(current_skin)

            if btn_goback.tick(events):
                run = False

            btn_goback.update()
            btn_left.update()
            btn_right.update()

            if current_skin == self.active_skin:
                btn_equip.text = "USING"
            else:
                btn_equip.text = "ACTIVATE"

            window.blit(background, (0, 0))
            # blit price
            font = pygame.font.SysFont('None', 50)
            price = font.render(f"Price: {self.skins[current_skin]['price']}", True, (230, 225, 240))
            window.blit(price, (550, 500))
            window.blit(skin_imgs[current_index], skin_imgs[current_index].get_rect(center=(600, 400)))
            btn_left.draw(window)
            btn_right.draw(window)
            btn_buy.draw(window)
            btn_equip.draw(window)
            btn_goback.draw(window)
            text.draw(window, self.score)

            pygame.display.flip()


# def level_1(score, level, player_obj):
#     run = True
#     pause = False
#     pause_image = pygame.image.load('Sprites/resume.png')
#     play_button = Button(515, 500, "Sprites/play/play")
#     player = player_obj
#     ghost = Ghost(700, 480)
#     background = Background()

#
#     beams = [
#         Beam(0, 620, 1),
#         Beam(250, 658, 1),
#         Beam(500, 620, 1),
#         Beam(700, 550, 0),  # duszek
#         # Beam(859, 550,1),
#         Beam(1240, 550, 1)
#     ]
#     door = Door(1270, 450)  # 1150
#
#     beams2 = []
#     coins = [
#         Coin(300, 620),
#         Coin(550, 590),
#     ]
#     serca = [Serce(750, 450)]
#
#     clock = pygame.time.Clock()
#     while run:
#         delta = clock.tick(30) / 1000
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
#                 run = False
#                 pygame.quit()
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
#                 pause = not pause
#         keys = pygame.key.get_pressed()
#
#         if pause:
#             window.blit(pause_image, (500, 300))
#             play_button.draw(window)
#             if play_button.tick():
#                 pause = not pause
#             pygame.display.update()
#             continue
#         background.draw(window)
#
#         player.tick(keys, beams, beams2, delta, ghost, background.x_cord)
#         ghost.tick(beams, beams2, player, 710.0, 980.0, delta)
#         background.tick(player)
#         # door.tick()
#
#         player.draw(window, background)
#         door.draw(window, background.x_cord)
#         ghost.draw(window, background.x_cord)
#         for beam in beams:
#             beam.draw(window, background.x_cord)
#         for beam2 in beams2:
#             beam2.tick(player)
#             beam2.draw(window, background.x_cord)
#         for coin in coins:
#             coin.tick()
#             coin.draw(window, background.x_cord)
#             if coin.hitbox.colliderect(player.hitbox):
#                 coins.remove(coin)
#                 score += 1
#         for serce in serca:
#             serce.draw(window, background.x_cord)
#
#             if serce.hitbox.colliderect(player.hitbox) and player.health < 100:
#                 serce.tick(player)
#                 serca.remove(serce)
#         text.draw(window, score)
#         pygame.display.update()
#
#         if player.tick(keys, beams, beams2, delta, ghost,
#                        background.x_cord) == 0:
#             resume(0, level, player)
#         if player.y_cord > 750.0:
#             player.alive = False
#             resume(0, level, player)
#
#         if door.hitbox.colliderect(player.hitbox):
#             level += 1
#             resume(score, level, player)

# def level_2(score, level, player_obj):
#     run = True
#     pause = False
#     pause_image = pygame.image.load('Sprites/resume.png')
#     play_button = Button(515, 500, "Sprites/play/play")
#     player = player_obj
#     player.init_physics()
#     ghost = Ghost(875, 580)  # resp duszka
#     background = Background()
#     clock = 0
#     text = Text(950, 10)
#     door = Door(1800, 550)
#     ingamescore = 0
#
#     beams = [
#         Beam(0, 500, 1),  # 720 max na dole
#         Beam(250, 650, 1),
#         Beam(870, 650, 0),  # duszek
#         # Beam(1029, 650, 1),#duszek
#         Beam(1300, 500, 1),
#         Beam(1650, 650, 1),
#         Beam(1809, 650, 1),
#     ]
#     beams2 = [
#         Beam2(450, 690),  # 500 x
#     ]
#     coins = [
#         Coin(330, 610),
#         Coin(1380, 430),
#     ]
#     serca = [Serce(900, 500)]
#     clock = pygame.time.Clock()
#     while run:
#         delta = clock.tick(35) / 1000
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
#                 run = False
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#                 pause = not pause
#         keys = pygame.key.get_pressed()
#
#         if pause:
#             window.blit(pause_image, (500, 300))
#             play_button.draw(window)
#             if play_button.tick():
#                 pause = not pause
#             pygame.display.update()
#             continue
#
#         player.tick(keys, beams, beams2, delta, [ghost, beams2],
#                     background.x_cord)
#         ghost.tick(beams, beams2, player, 880.0, 1150.0, delta)
#         # odkad duszek sie porusza
#         background.tick(player)
#         door.tick()
#
#         background.draw(window)
#         player.draw(window, background)
#         ghost.draw(window, background.x_cord)
#         door.draw(window, background.x_cord)
#         for beam in beams:
#             beam.draw(window, background.x_cord)
#         for beam2 in beams2:
#             beam2.tick(player)
#             beam2.draw(window, background.x_cord)
#         for coin in coins:
#             coin.tick()
#             coin.draw(window, background.x_cord)
#             if coin.hitbox.colliderect(player.hitbox):
#                 coins.remove(coin)
#                 score += 1
#                 ingamescore += 1
#         for serce in serca:
#
#             serce.draw(window, background.x_cord)
#             if serce.hitbox.colliderect(player.hitbox) and player.health < 100:
#                 serce.tick(player)
#                 serca.remove(serce)
#         text.draw(window, score)
#         pygame.display.update()
#
#         if player.tick(keys, beams, beams2, delta, [
#             ghost,
#         ], background.x_cord) == 0:
#             resume(score - ingamescore, level, player)
#         if player.y_cord > 750.0:
#             player.alive = False
#             resume(score - ingamescore, level, player)
#
#         if door.hitbox.colliderect(player.hitbox):
#             level += 1
#             resume(score, level, player)

# def level_3(score, level, player_obj):
#     run = True
#     pause = False
#     pause_image = pygame.image.load('Sprites/resume.png')
#     play_button = Button(515, 500, "Sprites/play/play")
#     player = player_obj
#     player.init_physics()
#     ghost = Ghost(850, 480)  # resp duszka
#     background = Background()
#     clock = 0
#     text = Text(950, 10)
#     door = Door(1900, 100)  # 1900, 100
#     ingamescore = 0
#
#     beams = [
#         Beam(0, 400, 1),  # 720 max na dole
#         Beam(250, 500, 2),
#         Beam(450, 650, 1),  # sciana 480!!!
#         Beam(700, 550, 0),  #
#         Beam(1020, 550, 1),
#         Beam(1250, 600, 1),
#         Beam(1450, 500, 1),
#         Beam(1700, 430, 2),
#         Beam(1850, 350, 1),
#     ]
#     beams2 = [
#         Beam2(450, 635),  # 500 x
#         Beam2(815, 533),
#     ]
#     coins = [
#         Coin(250, 480),
#         Coin(730, 520),
#         Coin(1500, 470),
#     ]
#     serca = [
#         Serce(500, 550),
#         Serce(1290, 500),
#
#     ]
#     clock = pygame.time.Clock()
#     while run:
#         delta = clock.tick(35) / 1000
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
#                 run = False
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#                 pause = not pause
#         keys = pygame.key.get_pressed()
#
#         if pause:
#             window.blit(pause_image, (500, 300))
#             play_button.draw(window)
#             if play_button.tick():
#                 pause = not pause
#             pygame.display.update()
#             continue
#
#         player.tick(keys, beams, beams2, delta, [ghost, beams2],
#                     background.x_cord)
#         ghost.tick(beams, beams2, player, 880.0, 1090.0, delta)
#         # odkad duszek sie porusza
#         background.tick(player)
#         door.tick()
#
#         background.draw(window)
#         player.draw(window, background)
#         ghost.draw(window, background.x_cord)
#         door.draw(window, background.x_cord)
#         for beam in beams:
#             beam.draw(window, background.x_cord)
#         for beam2 in beams2:
#             beam2.tick(player)
#             beam2.draw(window, background.x_cord)
#         for coin in coins:
#             coin.tick()
#             coin.draw(window, background.x_cord)
#             if coin.hitbox.colliderect(player.hitbox):
#                 coins.remove(coin)
#                 score += 1
#                 ingamescore += 1
#         for serce in serca:
#
#             serce.draw(window, background.x_cord)
#             if serce.hitbox.colliderect(player.hitbox) and player.health < 100:
#                 serce.tick(player)
#                 serca.remove(serce)
#         text.draw(window, score)
#         pygame.display.update()
#
#         if player.tick(keys, beams, beams2, delta, [
#             ghost,
#         ], background.x_cord) == 0:
#             resume(score - ingamescore, level, player)
#         if player.y_cord > 750.0:
#             player.alive = False
#
#             resume(score - ingamescore, level, player)
#
#         if door.hitbox.colliderect(player.hitbox):
#             level += 1
#             resume(score, level, player)

# def level_4(score, level, player_obj):
#     run = True
#     pause = False
#     pause_image = pygame.image.load('Sprites/resume.png')
#     play_button = Button(515, 500, "Sprites/play/play")
#     player = player_obj
#     player.init_physics()
#     ghost = Ghost(980, 520)
#     background = Background()
#     clock = 0
#     ingamescore = 0
#     text = Text(950, 10)
#     beams = [
#         Beam(0, 600, 1),
#         Beam(250, 650, 2),
#         Beam(350, 600, 1),
#         Beam(600, 670, 1),
#         Beam(800, 600, 1),
#         Beam(950, 600, 0),
#         Beam(1270, 600, 0),
#         Beam(1430, 600, 1),
#
#     ]
#     door = Door(1470, 400)
#     beams2 = [
#         Beam2(800, 350),
#         Beam2(1250, 580),
#     ]
#     coins = [
#         Coin(240, 630),
#         Coin(650, 640),
#     ]
#     serca = [
#         Serce(380, 500),
#         Serce(1340, 510),
#     ]
#
#     clock = pygame.time.Clock()
#     while run:
#         delta = clock.tick(35) / 1000
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
#                 run = False
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#                 pause = not pause
#         keys = pygame.key.get_pressed()
#
#         if pause:
#             window.blit(pause_image, (500, 300))
#             play_button.draw(window)
#             if play_button.tick():
#                 pause = not pause
#             pygame.display.update()
#             continue
#
#         player.tick(keys, beams, beams2, delta, [ghost, beams2],
#                     background.x_cord)
#         ghost.tick(beams, beams2, player, 990.0, 1120.0, delta)
#         background.tick(player)
#         door.tick()
#
#         background.draw(window)
#         player.draw(window, background)
#         door.draw(window, background.x_cord)
#         ghost.draw(window, background.x_cord)
#         for beam in beams:
#             beam.draw(window, background.x_cord)
#         for beam2 in beams2:
#             beam2.tick(player)
#             beam2.draw(window, background.x_cord)
#         for coin in coins:
#             coin.tick()
#             coin.draw(window, background.x_cord)
#             if coin.hitbox.colliderect(player.hitbox):
#                 coins.remove(coin)
#                 score += 1
#                 ingamescore += 1
#         for serce in serca:
#
#             serce.draw(window, background.x_cord)
#             if serce.hitbox.colliderect(player.hitbox) and player.health < 100:
#                 serce.tick(player)
#                 serca.remove(serce)
#         text.draw(window, score)
#         pygame.display.update()
#
#         if player.tick(keys, beams, beams2, delta, [
#             ghost,
#         ], background.x_cord) == 0:
#             resume(score - ingamescore, level, player)
#         if player.y_cord > 750.0:
#             player.alive = False
#
#             resume(score - ingamescore, level, player)
#
#         if door.hitbox.colliderect(player.hitbox):
#             level += 1
#             resume(score, level, player)

# def level_5(score, level, player_obj):
#     run = True
#     pause = False
#     pause_image = pygame.image.load('Sprites/resume.png')
#     play_button = Button(515, 500, "Sprites/play/play")
#     player = player_obj
#     player.init_physics()
#     ghost = Ghost(660, 580)
#     background = Background()
#     clock = 0
#     ingamescore = 0
#     text = Text(950, 10)
#     beams = [Beam(0, 600, 1), Beam(250, 650, 2), Beam(350, 600, 1), ]
#     door = Door(1500, 400)
#     beams2 = [
#         Beam2(900, 670),
#     ]
#     coins = [
#         Coin(200, 650),
#         Coin(700, 610),
#     ]
#     serca = [Serce(800, 500)]
#
#     clock = pygame.time.Clock()
#     while run:
#         delta = clock.tick(35) / 1000
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
#                 run = False
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#                 pause = not pause
#         keys = pygame.key.get_pressed()
#
#         if pause:
#             window.blit(pause_image, (500, 300))
#             play_button.draw(window)
#             if play_button.tick():
#                 pause = not pause
#             pygame.display.update()
#             continue
#
#         player.tick(keys, beams, beams2, delta, [ghost, beams2],
#                     background.x_cord)
#         ghost.tick(beams, beams2, player, 670.0, 920.0, delta)
#         background.tick(player)
#         door.tick()
#
#         background.draw(window)
#         player.draw(window, background)
#         door.draw(window, background.x_cord)
#         ghost.draw(window, background.x_cord)
#         for beam in beams:
#             beam.draw(window, background.x_cord)
#         for beam2 in beams2:
#             beam2.tick(player)
#             beam2.draw(window, background.x_cord)
#         for coin in coins:
#             coin.tick()
#             coin.draw(window, background.x_cord)
#             if coin.hitbox.colliderect(player.hitbox):
#                 coins.remove(coin)
#                 score += 1
#                 ingamescore += 1
#         for serce in serca:
#
#             serce.draw(window, background.x_cord)
#             if serce.hitbox.colliderect(player.hitbox) and player.health < 100:
#                 serce.tick(player)
#                 serca.remove(serce)
#         text.draw(window, score)
#         pygame.display.update()
#
#         if player.tick(keys, beams, beams2, delta, [ghost, ], background.x_cord) == 0:
#             resume(score - ingamescore, level, player)
#         if player.y_cord > 750.0:
#             player.alive = False
#             resume(score - ingamescore, level, player)
#
#         if door.hitbox.colliderect(player.hitbox):
#             level += 1
#             resume(score, level, player)

# def resume(score, level, player: Player):
#     run = True
#     clock = 0
#
#     background = pygame.image.load('Sprites/main menu/menu_background.png')
#
#     play_button = Button(515, 500, "Sprites/next_level/next")
#     shop_button = Button(900, 500, "Sprites/next_level/next")
#     menu_button = Button(100, 500, "Sprites/next_level/next")
#
#     if not player.alive:
#         player.health = 100
#         player.alive = True  # reset player if it died
#         print("reset player")
#     c = pygame.time.Clock()
#     while run:
#         clock += c.tick(60) / 1000  # maksymalnie 60 fps
#         events = pygame.event.get()
#         for event in events:
#             if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
#                 pygame.quit()
#                 run = False
#
#         if play_button.tick():
#             if level == 1:
#                 player.x_cord = 0
#                 player.y_cord = 0
#                 level_1(0, level, player)
#             if level == 2:
#                 level_2(score, level, player)
#             if level == 3:
#                 level_3(score, level, player)
#             if level == 4:
#                 level_4(score, level, player)
#             if level == 5:
#                 level_5(score, level, player)
#
#         if shop_button.tick():
#             shop(score, level, player)
#
#         if menu_button.tick():
#             menu(score, level, player)
#
#         window.blit(background, (0, 0))
#         play_button.draw(window)
#         shop_button.draw(window)
#         menu_button.draw(window)
#
#         pygame.display.update()

# def menu(score, level, player: Player):
#     start_level = {1: level_1,
#                    2: level_2,
#                    3: level_3,
#                    4: level_4,
#                    5: level_5,
#                    6: level_6,
#                    }
#
#     run = True
#     clock = pygame.time.Clock()
#     background = pygame.image.load('Sprites/main menu/menu_background.png').convert_alpha()
#
#     active = [True if i in start_level.keys() is not None else False for i in range(1, 11)]
#
#     level_buttons = []
#     font = pygame.font.SysFont('None', 50)
#     for i in range(10):
#         if active[i]:
#             btn = ButtonLevelMenu(170 + 200 * (i % 5), 400 + 150 * (i // 5), f"{i + 1}")
#             level_buttons.append(btn)
#
#     while run:
#         clock.tick(60)  # maksymalnie 60 fps
#         events = pygame.event.get()
#         for event in events:
#             if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
#                 run = False
#
#         for btn in level_buttons:
#             btn.update()
#
#         for i in range(10):
#             if active[i] and level_buttons[i].tick(events):
#                 level = i + 1
#                 start_level[level](score, level, player)
#
#         window.blit(background, (0, 0))
#
#         # draw title
#         font = pygame.font.SysFont('None', 100)
#         title = font.render("Chose your level : ", True, (230, 225, 240))
#         window.blit(title, (50, 300))
#         for btn in level_buttons:
#             btn.draw(window)
#
#         pygame.display.update()


def main(first_level):
    run = True

    player = Player('John')
    game = Game(player)

    background = pygame.image.load('Sprites/main menu/menu_background.png')
    play_button = Button(105, 400, "Sprites/main menu/play_button")

    clock = pygame.time.Clock()
    time = 0
    while run:
        time += clock.tick(60) / 1000  # maksymalnie 60 fps
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                run = False

        if play_button.tick():
            game.load_level(first_level())
            game.run()
            run = False

        window.blit(background, (0, 0))
        play_button.draw(window)

        pygame.display.update()


def level_editor(level_to_edit):
    def print_format(level: dict):
        """
        Prints the level in the correct format to then copy and paste it to the according function
        """
        print("{")
        print(f"'nb_level' : {level['nb_level']},")
        print(f"'beams' : [")
        for beam in level['beams']:
            print(f"Beam({beam.x_cord}, {beam.y_cord}, {beam.number}, rotation={beam.rotation}),")
        print("],")

        print(f"'coins' : [")
        for coin in level['coins']:
            print(f"Coin({coin.x_cord}, {coin.y_cord}),")
        print("],")

        print(f"'beams2' : [")
        for beam2 in level['beams2']:
            print(f"Beam2({beam2.x_cord}, {beam2.y_cord}, rotation={beam2.rotation}),")
        print("],")

        print(f"'ghosts' : [")
        for ghost in level['ghosts']:
            print(f"Ghost({ghost.x_cord}, {ghost.y_cord}),")
        print("],")

        print(f"'serce' : [")
        for heart in level['serce']:
            print(f"Serce({heart.x_cord}, {heart.y_cord}),")
        print("],")

        if level['door']:
            print(f"'door' : Door({level['door'].x_cord}, {level['door'].y_cord}),")

        print("background:Camera(),")
        print("}")
        print()

    run = True
    clock = pygame.time.Clock()

    level = level_to_edit()

    beam_img = pygame.image.load('trawa160X40.png')
    beam_img.set_alpha(100)

    coin_img = pygame.image.load('Sprites/coin.png')
    coin_img.set_alpha(100)

    beam2_img = pygame.image.load('Sprites/spikes.png')
    beam2_img.set_alpha(100)

    ghost_img = pygame.image.load('Sprites/ghost.png')
    ghost_img.set_alpha(100)

    heart_img = pygame.image.load('Sprites/heart.png')
    heart_img.set_alpha(100)

    door_img = pygame.image.load('Sprites/drzwi.png')
    door_img.set_alpha(100)

    player = Player('John')
    editor_game = Game(player)

    imgs = {"beam": beam_img,
            "coin": coin_img,
            "beam2": beam2_img,
            "ghost": ghost_img,
            "heart": heart_img,
            "door": door_img
            }
    selected = "beam"

    # list to store actions taken in the level editor
    actions = []

    rotation = 0
    while run:

        clock.tick(60)
        editor_game.load_level(level)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if selected == "beam":
                    # create a new beam object and add it to the level
                    beam = Beam(event.pos[0] - editor_game.camera.x_cord, event.pos[1] - editor_game.camera.y_cord,
                                1, rotation=rotation)
                    level["beams"].append(beam)
                    # store the action in the actions list
                    actions.append({"type": "add", "object": "beam", "data": beam})

                elif selected == "coin":
                    # create a new coin object and add it to the level
                    coin = Coin(event.pos[0] - editor_game.camera.x_cord, event.pos[1] - editor_game.camera.y_cord)
                    level["coins"].append(coin)
                    # store the action in the actions list
                    actions.append({"type": "add", "object": "coin", "data": coin})

                elif selected == "beam2":
                    beam2 = Beam2(event.pos[0] - editor_game.camera.x_cord,
                                  event.pos[1] - editor_game.camera.y_cord,
                                  rotation=rotation)
                    level["beams2"].append(beam2)
                    actions.append({"type": "add", "object": "beam2", "data": beam2})

                elif selected == "ghost":
                    ghost = Ghost(event.pos[0] - editor_game.camera.x_cord,
                                  event.pos[1] - editor_game.camera.y_cord)
                    level["ghosts"].append(ghost)
                    actions.append({"type": "add", "object": "ghost", "data": ghost})

                elif selected == "heart":
                    heart = Serce(event.pos[0] - editor_game.camera.x_cord,
                                  event.pos[1] - editor_game.camera.y_cord)
                    level["serce"].append(heart)
                    actions.append({"type": "add", "object": "heart", "data": heart})

                elif selected == "door":
                    door = Door(event.pos[0] - editor_game.camera.x_cord,
                                event.pos[1] - editor_game.camera.y_cord)
                    level["door"] = door
                    actions.append({"type": "add", "object": "door", "data": door})

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print_format(level)
                if event.key == pygame.K_c:
                    selected = "coin"
                if event.key == pygame.K_b:
                    selected = "beam"
                if event.key == pygame.K_s:
                    selected = "beam2"
                if event.key == pygame.K_g:
                    selected = "ghost"
                if event.key == pygame.K_h:
                    selected = "heart"
                if event.key == pygame.K_d:
                    selected = "door"

                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    if actions:
                        # get the last action from the actions list
                        last_action = actions.pop()
                        if last_action["type"] == "add":
                            # remove the object from the level
                            if last_action["object"] == "beam":
                                level["beams"].remove(last_action["data"])
                            elif last_action["object"] == "coin":
                                level["coins"].remove(last_action["data"])
                            elif last_action["object"] == "beam2":
                                level["beams2"].remove(last_action["data"])
                            elif last_action["object"] == "ghost":
                                level["ghosts"].remove(last_action["data"])
                            elif last_action["object"] == "heart":
                                level["serce"].remove(last_action["data"])
                            elif last_action["object"] == "door":
                                level["door"] = None
                if event.key == pygame.K_r:
                    rotation += 1
                    rotation %= 4

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            editor_game.camera.x_cord -= 10
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            editor_game.camera.x_cord += 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            editor_game.camera.y_cord += 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            editor_game.camera.y_cord -= 10

        # bounds
        if editor_game.camera.x_cord > 0:
            editor_game.camera.x_cord = 0
        if editor_game.camera.y_cord > 0:
            editor_game.camera.y_cord = 0
        if editor_game.camera.x_cord < -editor_game.camera.width + resolution[0]:
            editor_game.camera.x_cord = -editor_game.camera.width + resolution[0]
        if editor_game.camera.y_cord < -editor_game.camera.height + resolution[1]:
            editor_game.camera.y_cord = -editor_game.camera.height + resolution[1]

        editor_game.draw()
        img_to_show = imgs[selected]
        img_to_show = pygame.transform.rotate(img_to_show, rotation * 90)

        window.blit(img_to_show, pygame.mouse.get_pos())
        pygame.display.flip()


if __name__ == "__main__":
    main(level_1)
