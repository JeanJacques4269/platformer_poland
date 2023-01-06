import pygame
from math import floor, sqrt, degrees, asin
from tools.colors import *

resolution = (1280, 720)


class Physic:

    def __init__(self, x, y, width, height, acc, max_vel):
        self.x_cord = x  # współrzędna x
        self.y_cord = y  # współrzędna y
        self.hor_velocity = 0  # prędkość w poziomie
        self.ver_velocity = 0  # prędkość w pionie
        self.acc = acc  # przyspieszenie
        self.max_vel = max_vel / 1.5  # maksymalna prędkość
        self.width = width  # szerokość
        self.height = height  # wysokość
        self.previous_x = x
        self.previous_y = y
        self.jumping = False  # czy skacze
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width,
                                  self.height)
        self.gravity = 0.7

    def physic_tick(self, beams, beams2):
        self.ver_velocity += self.gravity
        self.x_cord += self.hor_velocity
        self.y_cord += self.ver_velocity
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

        # check collision with beams
        for beam in beams:
            if beam.hitbox.colliderect(self.hitbox):
                if self.x_cord + self.width >= beam.x_cord + 1 > self.previous_x + self.width:
                    self.x_cord = self.previous_x
                    self.hor_velocity = 0
                if self.x_cord <= beam.x_cord + beam.width - 1 < self.previous_x:
                    self.x_cord = self.previous_x
                    self.hor_velocity = 0
                if self.y_cord + self.height >= beam.y_cord + 1 > self.previous_y + self.height:
                    self.y_cord = self.previous_y - 1
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y_cord <= beam.y_cord + beam.height - 1 < self.previous_y:
                    self.y_cord = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False

        # check collision with beams2
        for beam2 in beams2:
            if beam2.hitbox.colliderect(self.hitbox):
                if self.x_cord + self.width >= beam2.x_cord + 1 > self.previous_x + self.width:
                    self.x_cord = self.previous_x
                    self.hor_velocity = 0
                if self.x_cord <= beam2.x_cord + beam2.width - 1 < self.previous_x:
                    self.x_cord = self.previous_x
                    self.hor_velocity = 0
                if self.y_cord + self.height >= beam2.y_cord + 1 > self.previous_y + self.height:
                    self.y_cord = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y_cord <= beam2.x_cord + beam2.width - 1 < self.previous_y:
                    self.y_cord = self.previous_y
                    self.ver_velocity = 0

        self.previous_x = self.x_cord
        self.previous_y = self.y_cord


class Health:

    def __init__(self, max_health=100):
        self.health = max_health
        self.max_health = max_health  # ilość punktów życia
        self.alive = True  # czy obiekt żyje
        self.last_dmg = 0  # czas od ostatnich obrażeń

    def health_tick(self, delta_tm):
        self.last_dmg += delta_tm

    def dealt_damage(self, damage, hit_speed):
        if self.last_dmg > hit_speed:
            self.health -= damage
            self.last_dmg = 0
            if self.health <= 0:
                self.health = 0
                self.alive = False

    def draw_health(self, win, x, y, max_width, height):
        percent_width = self.health / self.max_health
        width = round(max_width * percent_width)
        if self.health < 40:
            color = (255, 30, 30)
        elif self.health < 70:
            color = (255, 214, 77)
        else:
            color = (30, 255, 30)

        pygame.draw.rect(win, (30, 30, 30), (x, y, max_width, height))
        pygame.draw.rect(win, color, (x, y, width, height))


class Button:

    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_image = pygame.image.load(f"{file_name}.png")
        self.hovered_button_image = pygame.image.load(
            f"{file_name}_hovered.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord,
                                  self.button_image.get_width(),
                                  self.button_image.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.hovered_button_image, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_image, (self.x_cord, self.y_cord))


class ButtonLevelMenu:
    """
    Button class for level menu (optimized for it)
    """

    def __init__(self, x, y, text, width=100):
        """
        :param x: x_coord
        :param y: y_coord
        :param w: max width
        :param text: text
        :param back_color: can be (-1,-1,-1) for transparent
        :param text_color: text color
        :param font: font
        :param onclick: function to call when clicked
        """

        super().__init__()
        self.x = x
        self.y = y
        self.w = width
        self.h = 100

        self.text = text
        self.font = pygame.font.SysFont("None", 50)

        self.back_color = LIGHTERBLACK

        self.textcolor = DARKWHITE

        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)

        self.selected = False

    def update(self):
        if pygame.mouse.get_pressed()[0] and self.selected:
            if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                # shrink
                self.hitbox = pygame.Rect(self.x + 5, self.y + 5, 90, 90)

        else:
            self.hitbox = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, win):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            self.back_color = LIGHTBLACK
        else:
            self.back_color = LIGHTERBLACK
        pygame.draw.rect(win, self.back_color, self.hitbox)
        text = self.font.render(self.text, True, self.textcolor)

        # center text in button
        win.blit(text, (self.x + (self.w - text.get_width()) / 2, self.y + (self.h - text.get_height()) / 2))

    def tick(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hitbox.collidepoint(
                    pygame.mouse.get_pos()):
                self.selected = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.selected:
                if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                    return True
                else:
                    self.selected = False


class ButtonImg:
    """
    Button class for level menu (optimized for it)
    """

    def __init__(self, x, y, file):
        """
        :param x: x_coord
        :param y: y_coord
        :param w: max width
        :param text: text
        :param back_color: can be (-1,-1,-1) for transparent
        :param text_color: text color
        :param font: font
        :param onclick: function to call when clicked
        """

        super().__init__()
        self.x = x
        self.y = y

        self.img = pygame.image.load(f"{file}.png")
        self.img_hover = pygame.image.load(f"{file}_hovered.png")

        self.current_img = self.img
        self.rect = self.img.get_rect(topleft=(self.x, self.y))
        self.selected = False

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and self.selected:
                self.current_img = self.img_hover
        else:
            self.current_img = self.img

    def draw(self, win):
        win.blit(self.current_img, self.rect)

    def tick(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(
                    pygame.mouse.get_pos()):
                self.selected = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.selected:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    return True
                else:
                    self.selected = False


class Serce:

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.image = pygame.image.load("Sprites/heart.PNG")
        self.width, self.height = self.image.get_size()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width,
                                  self.height)

    def tick(self, player):
        player.dealt_damage(-34, 0.5)

    def draw(self, win, background):
        win.blit(self.image, (self.x_cord + background.x_cord, self.y_cord + background.y_cord))


class Coin:

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.image = pygame.image.load("Sprites/coin.png")
        self.width, self.height = self.image.get_size()

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width,
                                  self.height)

    def draw(self, win, background):
        win.blit(self.image, (self.x_cord + background.x_cord, self.y_cord + background.y_cord))


class Door:

    def __init__(self, x, y):
        self.hitbox = None
        self.x_cord = x
        self.y_cord = y
        self.image = pygame.image.load("Sprites/drzwi.png")
        self.width, self.height = self.image.get_size()
        self.tick()

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, win, background):
        win.blit(self.image, (self.x_cord + background.x_cord, self.y_cord + background.y_cord))


class Text:

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y

    def draw(self, window, score):
        text_score = pygame.font.Font.render(pygame.font.SysFont("arial", 48),
                                             f"Score: {score}", True,
                                             (0, 0, 0))
        window.blit(text_score, (self.x_cord, self.y_cord))


class Player(Physic, Health):

    def __init__(self, name):
        Health.__init__(self, 100)
        self.stand_right_img = None
        self.stand_left_img = None
        self.jump_right_img = None
        self.jump_left_img = None
        self.walk_right_img = None
        self.walk_left_img = None
        self.walk_index = 0
        self.direction = 1
        self.load_skin(name)
        self.init_physics()

    def tick(self, keys, beams, beams2, delta_tm):  # wykonuje się raz na powtórzenie pętli
        self.physic_tick(beams, beams2)
        self.health_tick(delta_tm)

        if not self.alive:
            return

        if keys[pygame.K_LSHIFT] and abs(self.hor_velocity) > 0:
            self.hor_velocity = 10 * self.direction

        if keys[pygame.K_a] and self.hor_velocity > self.max_vel * -1:
            self.hor_velocity -= self.acc
        if keys[pygame.K_d] and self.hor_velocity < self.max_vel:
            self.hor_velocity += self.acc
        if keys[pygame.K_SPACE] and self.jumping is False:
            self.ver_velocity -= 20
            self.jumping = True
        if self.hor_velocity > 0:
            self.direction = 1
        elif self.hor_velocity < 0:
            self.direction = -1
        if not (keys[pygame.K_d] or keys[pygame.K_a]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc

    def draw(self, win, camera):
        x_screen = self.x_cord + camera.x_cord
        y_screen = self.y_cord + camera.y_cord

        self.draw_health(win, x_screen, y_screen - 15, self.width, 10)

        if self.jumping:
            image = self.jump_left_img if self.direction == -1 else self.jump_right_img
        elif self.hor_velocity != 0:
            image = self.walk_left_img[floor(self.walk_index)] if self.direction == -1 else self.walk_right_img[
                floor(self.walk_index)]
            self.walk_index += 0.4
            if self.walk_index > 5:
                self.walk_index = 0
        else:
            image = self.stand_left_img if self.direction == -1 else self.stand_right_img

        win.blit(image, (x_screen, y_screen))

    def init_physics(self):
        width = self.stand_right_img.get_width()  # szerokość
        height = self.stand_right_img.get_height()  # wysokość
        Physic.__init__(self, 0, 0, width, height, 0.5, 5)

    def load_skin(self, name):
        self.stand_right_img = pygame.image.load(f'Sprites/characters/{name}/stand.png')
        self.stand_left_img = pygame.transform.flip(pygame.image.load(f'Sprites/characters/{name}/stand.png'), True, False)
        self.jump_right_img = pygame.image.load(f'Sprites/characters/{name}/jump.png')
        self.jump_left_img = pygame.transform.flip(pygame.image.load(f'Sprites/characters/{name}/jump.png'), True, False)
        self.walk_right_img = [pygame.image.load(f'Sprites/characters/{name}/klatka0{x}.png') for x in range(1, 7)]
        self.walk_left_img = [pygame.transform.flip(pygame.image.load(f'Sprites/characters/{name}/klatka0{x}.png'), True, False)
                              for x in range(1, 7)]
        self.walk_index = 0
        self.direction = 1
        self.init_physics()


class Ghost(Physic, Health):

    def __init__(self, x, y):
        self.start_x = x
        self.image = pygame.image.load("Sprites/ghost.png")
        width, height = self.image.get_size()
        Health.__init__(self, 100)
        Physic.__init__(self, x, y, width, height, 1, 3)
        self.gravity = 0.0
        self.go_left()

    def go_left(self):
        if -self.hor_velocity < self.max_vel:
            self.hor_velocity -= self.acc

    def go_right(self):
        if self.hor_velocity < self.max_vel:
            self.hor_velocity += self.acc

    def tick(self, beams, beams2, player, x1, x2, delta_tm):
        self.physic_tick(beams, beams2)
        self.health_tick(delta_tm)

        if self.hitbox.colliderect(player.hitbox):
            player.dealt_damage(34, 0.5)  # zadaj dwadzieścia obrażeń
            if self.x_cord < player.x_cord:
                self.go_left()
                self.go_left()
            if self.x_cord > player.x_cord:
                self.go_right()
                self.go_right()
        else:
            if self.x_cord > x2:
                self.go_left()

            elif self.x_cord < x1:
                self.go_right()

    def draw(self, win, background):

        win.blit(self.image, (self.x_cord + background.x_cord, self.y_cord + background.y_cord))
        self.draw_health(win, self.x_cord + background.x_cord, self.y_cord + background.y_cord - 15,
                         self.width, 10)


class Beam2:

    def __init__(self, x, y, rotation=0):
        self.x_cord = x
        self.y_cord = y
        self.rotation = rotation
        self.image = pygame.image.load("Sprites/spikes.png")
        self.width, self.height = self.image.get_size()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width,
                                  self.height)
        self.image = pygame.transform.rotate(self.image, rotation * 90)

    def tick(self, player):
        if self.hitbox.colliderect(player.hitbox):
            player.dealt_damage(34, 0.5)

    def draw(self, win, background):
        win.blit(
            self.image,
            (self.x_cord + background.x_cord, self.y_cord + background.y_cord, self.width, self.height))


class Beam:

    def __init__(self, x, y, number, rotation=0):
        """
        :param x:
        :param y:
        :param number:
        :param rotation: 0 - horizontal, 1 - rotation
        """
        self.x_cord = x
        self.y_cord = y
        self.number = number
        self.rotation = rotation
        if number == 2:
            self.image = pygame.image.load("trawa_gora40x40.png")
        elif number == 1:
            self.image = pygame.image.load("trawa160X40.png")
        elif number == 0:
            self.image = pygame.image.load("trawa320X40.png")

        self.image = pygame.transform.rotate(self.image, rotation * 90)
        self.width, self.height = self.image.get_size()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width,
                                  self.height)

    def draw(self, win, background):

        win.blit(self.image,
                 (self.x_cord + background.x_cord, self.y_cord + background.y_cord, self.width, self.height)
                 )

    def __repr__(self):
        return f"Beam({self.x_cord}, {self.y_cord}, {self.number})"


class Camera:
    """used to be called Background"""

    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("Sprites/forest_bigger.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def tick(self, player):
        """smooth camera movement"""
        half_screen_width = resolution[0] / 2
        three_quarter_screen_height = resolution[1] * 5 / 8
        # horizontal movement
        target_x_cord = 0
        if player.x_cord < half_screen_width:
            target_x_cord = 0
        elif player.x_cord > self.width - half_screen_width:
            target_x_cord = -self.width + resolution[0]
        else:
            target_x_cord = -player.x_cord + half_screen_width
        self.x_cord += (target_x_cord - self.x_cord) * 0.1

        # vertical movement
        target_y_cord = 0
        if player.y_cord < three_quarter_screen_height:
            target_y_cord = 0
        elif player.y_cord > self.height - three_quarter_screen_height:
            target_y_cord = -self.height + resolution[1]

        else:
            target_y_cord = three_quarter_screen_height - player.y_cord

        if target_y_cord - self.y_cord > 0:
            self.y_cord += (target_y_cord - self.y_cord) * 0.01
        else:
            self.y_cord += (target_y_cord - self.y_cord) * 0.03

    def draw(self, win):
        win.blit(self.image, (self.x_cord, self.y_cord))
