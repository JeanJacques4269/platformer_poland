import pygame
from tools.colors import *

BLACK = 0, 0, 0
GRAY = (185, 224, 226)

TEXTCOLORDEFAULT = 255, 255, 255
TEXTCOLORONHOVER = GRAY


class ButtonLevelMenu(pygame.sprite.Sprite):
    def __init__(self, x, y, text):
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
        self.w = 100
        self.h = 100

        self.text = text
        self.font = pygame.font.SysFont("None", 50)

        self.back_color = LIGHTERBLACK

        self.textcolor = DARKWHITE

        self.hitbox = pygame.Rect(self.x, self.y, 100, 100)

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                # shrink
                self.hitbox = pygame.Rect(self.x + 5, self.y + 5, 90, 90)
            else:
                pass
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
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            # if left click just got released
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    return True


class ButtonImg(pygame.sprite.Sprite):
    def __init__(self, img, x, y, onclick):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x, self.y = x, y
        self.pos = x, y
        self.onclick = onclick

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.isMouseOn(event.pos):
                    self.onclick()

    def isMouseOn(self, pos):
        return self.rect.collidepoint(*pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Checkbox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, checked):
        """
        :param x:
        :param y:
        :param w:
        """
        super().__init__()
        self.checked = checked
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.width = w
        self.rect = pygame.rect.Rect(x, y, w, w)

        self.outline = False

    def draw(self, win):
        if self.checked:
            a = 0
        else:
            a = 3
        pygame.draw.rect(win, BLACK, self.rect, a)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.isMouseOnIt(event.pos):
                    self.checked = False if self.checked else True

    def isMouseOnIt(self, pos):
        return self.rect.collidepoint(*pos)

    def hover(self):
        # self.back_color = self.hover_back_color
        # self.textcolor = RED
        self.outline = True

    def default(self):
        # self.back_color = self.default_back_color
        # self.textcolor = self.textcolor_default
        self.outline = False


_circle_cache = {}


def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points


# Code from stack overflow to render text with an outline
def render(text, font, gfcolor=pygame.Color('dodgerblue'), ocolor=(255, 255, 255), opx=2):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf
