import time

import pygame.display

from game import *
from tools.colors import *

pygame.init()
resolution = (1280, 720)
window = pygame.display.set_mode(resolution)


def empty_level() -> dict:
    """
    empty level holding dict
    """
    return {
        "nb_level": 7,
        'beams': [],
        'beams2': [],
        'coins': [],
        'ghosts': [],
        'door': None,
        'background': Camera(),
        'serce': [],
    }


def level_1():
    return {
        'nb_level': 1,
        'beams': [
            Beam(0, 620, 1, rotation=0),
            Beam(250, 658, 1, rotation=0),
            Beam(500, 620, 1, rotation=0),
            Beam(700, 550, 0, rotation=0),
            Beam(859, 550, 1, rotation=0),
            Beam(1200, 550, 1, rotation=0),
        ],
        'coins': [
            Coin(300, 620),
            Coin(550, 590),
        ],
        'beams2': [
        ],
        'ghosts': [
            Ghost(838, 473),
        ],
        'serce': [
            Serce(750, 450),
        ],
        'door': Door(1234, 349),
        "background": Camera(),

    }


def level_2():
    return {
        "nb_level": 2,
        'beams': [
            Beam(0, 500, 1),  # 720 max na dole
            Beam(250, 650, 1),
            Beam(870, 650, 0),  # duszek
            # Beam(1029, 650, 1),#duszek
            Beam(1300, 500, 1),
            Beam(1650, 650, 1),
            Beam(1809, 650, 1),
        ],
        'beams2': [Beam2(450, 690),  # 500 x
                   ],
        'coins': [
            Coin(330, 610),
            Coin(1380, 430),
        ],
        'ghosts': [Ghost(875, 580)],
        'door': Door(1800, 550),
        'background': Camera(),
        'serce': [Serce(900, 500)]
    }


def level_3():
    return {
        "nb_level": 3,
        'beams': [
            Beam(0, 400, 1),  # 720 max na dole
            Beam(250, 500, 2),
            Beam(450, 650, 1),  # sciana 480!!!
            Beam(700, 550, 0),  #
            Beam(1020, 550, 1),
            Beam(1250, 600, 1),
            Beam(1450, 500, 1),
            Beam(1700, 430, 2),
            Beam(1850, 350, 1),
        ],
        'beams2': [
            Beam2(450, 635),
            Beam2(815, 533)
        ],
        'coins': [
            Coin(250, 480),
            Coin(730, 520),
            Coin(1500, 470),
        ],
        'ghosts': [],
        'door': Door(1900, 100),
        'background': Camera(),
        'serce': [Serce(500, 550),
                  Serce(1290, 500), ]
    }


def level_4():
    return {
        "nb_level": 4,
        'beams': [
            Beam(0, 600, 1),
            Beam(250, 650, 2),
            Beam(350, 600, 1),
            Beam(600, 670, 1),
            Beam(800, 600, 1),
            Beam(950, 600, 0),
            Beam(1270, 600, 0),
            Beam(1430, 600, 1),

        ],
        'beams2': [
            Beam2(800, 350),
            Beam2(1250, 580),
        ],
        'coins': [
            Coin(240, 630),
            Coin(650, 640),
        ],
        'ghosts': [],
        'door': Door(1470, 400),
        'background': Camera(),
        'serce': [Serce(380, 500),
                  Serce(1340, 510), ]
    }


def level_5() -> dict:
    """
    I modified this level because yours was uncompleted
    """
    return {
        "nb_level": 6,
        'beams': [
            Beam(0, 600, 2),
            Beam(250, 600, 2),
            Beam(350, 600, 2),
            Beam(600, 600, 2),
            Beam(800, 600, 2),
            Beam(950, 600, 0),
            Beam(1270, 600, 0),
            Beam(1430, 600, 1),
        ],
        'beams2': [
            Beam2(800, 350),
            Beam2(1250, 580), ],
        'coins': [],
        'ghosts': [],
        'door': Door(1470, 400),
        'background': Camera(),
        'serce': [Serce(1150, 520), ],

    }


def level_6() -> dict:
    """
    I modified this level because yours was uncompleted
    """
    return {
        "nb_level": 6,
        'beams': [
            # Beginning
            Beam(0, 600, 0),
            Beam(320, 601, 0),
            Beam(640, 602, 0),

            # bridge
            Beam(960, 500, 1),
            Beam(1110, 400, 1),
            Beam(1260, 300, 1),
            Beam(1460, 300, 1),
            Beam(1610, 400, 1),
            Beam(1860, 500, 1),
            # link
            Beam(2010, 600, 0),
            Beam(2330, 601, 0),
            Beam(2650, 602, 0),

            # stairs
            Beam(2970, 600, 1),
            Beam(2970, 560, 1),

            Beam(3130, 600, 1),
            Beam(3130, 560, 1),
            Beam(3130, 520, 1),

            Beam(3290, 600, 1),
            Beam(3290, 560, 1),
            Beam(3290, 520, 1),
            Beam(3290, 480, 1),

            # pile
            Beam(3290, 640, 1),
            Beam(3290, 680, 1),
            Beam(3290, 720, 1),
            Beam(3290, 760, 1),
            Beam(3290, 800, 1),
            Beam(3290, 840, 1),
            Beam(3290, 880, 1),
            Beam(3290, 920, 1),

            # pile2
            Beam(3600, 40, 1),
            Beam(3600, 80, 1),
            Beam(3600, 120, 1),
            Beam(3600, 160, 1),
            Beam(3600, 200, 1),
            Beam(3600, 240, 1),
            Beam(3600, 280, 1),
            Beam(3600, 320, 0),

            Beam(3600, 440, 0),
            Beam(3600, 480, 1),
            Beam(3600, 520, 1),
            Beam(3600, 560, 1),
            Beam(3600, 600, 1),
            Beam(3600, 640, 1),
            Beam(3600, 680, 1),
            Beam(3600, 720, 1),
            Beam(3600, 760, 1),
            Beam(3740, 760, 1),

            # secret
            Beam(3920, 441, 0),
            Beam(3920, 320, 0),

            Beam(4200, 360, 2),
            Beam(4200, 400, 2),

            # way
            Beam(3450, 920, 0),
            Beam(3770, 921, 0),
            Beam(4090, 922, 0),
            Beam(4410, 923, 0),
            Beam(4730, 924, 0),

        ],
        'beams2': [Beam2(580, 590),
                   Beam2(640, 590),
                   Beam2(1610, 390),
                   Beam2(1650, 390),
                   Beam2(1690, 390),
                   Beam2(1730, 390),
                   ],
        'coins': [
            Coin(960 + 60, 500 - 30),
            Coin(1100 + 60, 400 - 30),
            Coin(1260 + 60, 300 - 30),
            Coin(1460 + 60, 300 - 30),
            Coin(1610 + 60, 400 - 30),
            Coin(1860 + 60, 500 - 30),

            Coin(3800, 440 - 30),
            Coin(3870, 440 - 30),
            Coin(3940, 440 - 30),
            Coin(4010, 440 - 30),
            Coin(4080, 440 - 30),

        ],
        'ghosts': [],
        'door': Door(4890, 925 - 200),
        'background': Camera(),
        'serce': [],

    }


def level_7() -> dict:
    return {
        'nb_level': 7,
        'beams': [
            Beam(990, 748, 1, rotation=0),
            Beam(1149, 748, 1, rotation=0),
            Beam(1307, 749, 1, rotation=0),
            Beam(1102, 599, 1, rotation=0),
            Beam(1102, 559, 1, rotation=0),
            Beam(1103, 519, 1, rotation=0),
            Beam(1102, 479, 1, rotation=0),
            Beam(1260, 599, 1, rotation=0),
            Beam(1260, 479, 1, rotation=0),
            Beam(1102, 438, 1, rotation=0),
            Beam(1100, 398, 1, rotation=0),
            Beam(1100, 358, 1, rotation=0),
            Beam(1258, 359, 1, rotation=0),
            Beam(1098, 318, 1, rotation=0),
            Beam(940, 317, 1, rotation=0),
            Beam(781, 316, 1, rotation=0),
            Beam(623, 315, 1, rotation=0),
            Beam(38, 665, 1, rotation=0),
            Beam(335, 314, 1, rotation=0),
            Beam(511, 172, 1, rotation=0),
            Beam(669, 172, 1, rotation=0),
            Beam(828, 172, 1, rotation=0),
            Beam(985, 171, 1, rotation=0),
            Beam(1142, 171, 1, rotation=0),
            Beam(1300, 171, 1, rotation=0),
            Beam(1459, 172, 1, rotation=0),
            Beam(1506, 318, 1, rotation=0),
            Beam(1618, 174, 1, rotation=0),
            Beam(1775, 174, 1, rotation=0),
            Beam(2223, 170, 1, rotation=0),
            Beam(2224, 210, 1, rotation=0),
            Beam(2225, 252, 1, rotation=0),
            Beam(2226, 292, 1, rotation=0),
            Beam(2227, 332, 1, rotation=0),
            Beam(2228, 373, 1, rotation=0),
            Beam(2228, 413, 1, rotation=0),
            Beam(2069, 412, 1, rotation=0),
            Beam(2073, 453, 1, rotation=0),
            Beam(2072, 493, 1, rotation=0),
            Beam(1913, 494, 1, rotation=0),
            Beam(1913, 534, 1, rotation=0),
            Beam(1913, 574, 1, rotation=0),
            Beam(1913, 614, 1, rotation=0),
            Beam(1913, 653, 1, rotation=0),
            Beam(1905, 783, 1, rotation=0),
            Beam(2063, 784, 1, rotation=0),
            Beam(2221, 784, 1, rotation=0),
            Beam(1747, 783, 1, rotation=0),
            Beam(1666, 319, 1, rotation=0),
            Beam(2379, 785, 1, rotation=0),
            Beam(196, 625, 1, rotation=0),
            Beam(196, 665, 1, rotation=0),
            Beam(198, 705, 1, rotation=0),
            Beam(198, 746, 1, rotation=0),
            Beam(356, 746, 1, rotation=0),
            Beam(515, 746, 1, rotation=0),
            Beam(673, 746, 1, rotation=0),
            Beam(833, 747, 1, rotation=0),
            Beam(20, 665, 1, rotation=0),
            Beam(1429, 750, 1, rotation=0),
            Beam(1550, 592, 1, rotation=1),
            Beam(1549, 438, 1, rotation=1),
            Beam(1551, 349, 1, rotation=1),
            Beam(1430, 790, 1, rotation=0),
            Beam(1591, 784, 1, rotation=0),
            Beam(1586, 784, 1, rotation=0),
            Beam(1589, 626, 1, rotation=1),
            Beam(1587, 468, 1, rotation=1),
            Beam(1591, 356, 1, rotation=1),
            Beam(1783, 196, 1, rotation=1),
            Beam(1742, 196, 1, rotation=1),
            Beam(2348, 9, 1, rotation=3),
        ],
        'coins': [
            Coin(1313, 554),
            Coin(1314, 431),
            Coin(2125, 349),
            Coin(1961, 441),
            Coin(382, 264),
            Coin(533, 324),
            Coin(2236, 124),
            Coin(1671, 274),
            Coin(1609, 274),
            Coin(1542, 273),
        ],
        'beams2': [
            Beam2(1528, 664, rotation=1),
            Beam2(1530, 594, rotation=1),
            Beam2(1531, 510, rotation=1),
            Beam2(1527, 437, rotation=1),
            Beam2(1632, 435, rotation=3),
            Beam2(1631, 508, rotation=3),
            Beam2(1628, 593, rotation=3),
            Beam2(1632, 660, rotation=3),
            Beam2(2329, 83, rotation=1),
            Beam2(1824, 265, rotation=3),
            Beam2(357, 673, rotation=3),
        ],
        'ghosts': [
            Ghost(750, 80),
            Ghost(1292, 80),
        ],
        'door': Door(2400, 785 - 200),
        'background': Camera(),
        'serce': [],

    }


def level_8():
    return {
        'nb_level': 8,
        'beams': [
            Beam(0, 1291, 1, rotation=0),
            Beam(158, 1292, 1, rotation=0),
            Beam(317, 1292, 1, rotation=0),
            Beam(317, 1252, 1, rotation=0),
            Beam(700, 1232, 1, rotation=0),
            Beam(1049, 1132, 1, rotation=0),
            Beam(1364, 977, 1, rotation=0),
            Beam(1365, 1017, 1, rotation=0),
            Beam(1365, 1057, 1, rotation=0),
            Beam(1365, 1097, 1, rotation=0),
            Beam(1364, 1137, 1, rotation=0),
            Beam(1363, 1176, 1, rotation=0),
            Beam(1363, 1214, 1, rotation=0),
            Beam(1521, 1215, 1, rotation=0),
            Beam(1679, 1215, 1, rotation=0),
            Beam(1838, 1216, 1, rotation=0),
            Beam(1996, 1216, 1, rotation=0),
            Beam(2155, 1215, 1, rotation=0),
            Beam(2313, 1216, 1, rotation=0),
            Beam(2470, 1217, 1, rotation=0),
            Beam(2468, 1177, 1, rotation=0),
            Beam(2626, 1178, 1, rotation=0),
            Beam(2630, 1217, 1, rotation=0),
            Beam(2626, 1140, 1, rotation=0),
            Beam(2626, 1101, 1, rotation=0),
            Beam(2783, 1064, 1, rotation=0),
            Beam(2940, 1025, 1, rotation=0),
            Beam(2693, 866, 1, rotation=0),
            Beam(2534, 866, 1, rotation=0),
            Beam(2534, 827, 1, rotation=0),
            Beam(2377, 827, 1, rotation=0),
            Beam(2378, 1014, 1, rotation=0),
            Beam(2225, 1012, 1, rotation=0),
            Beam(2069, 1012, 1, rotation=0),
            Beam(2220, 827, 1, rotation=0),
            Beam(2067, 972, 1, rotation=0),
            Beam(2066, 933, 1, rotation=0),
            Beam(2064, 895, 1, rotation=0),
            Beam(2063, 856, 1, rotation=0),
            Beam(2063, 828, 1, rotation=0),
            Beam(2062, 788, 1, rotation=0),
            Beam(2061, 750, 1, rotation=0),
            Beam(2059, 711, 1, rotation=0),
            Beam(2060, 672, 1, rotation=0),
            Beam(2060, 632, 1, rotation=0),
            Beam(2059, 592, 1, rotation=0),
            Beam(2059, 553, 1, rotation=0),
            Beam(2058, 513, 1, rotation=0),
            Beam(2057, 472, 1, rotation=0),
            Beam(2056, 432, 1, rotation=0),
            Beam(2218, 672, 1, rotation=0),
            Beam(2056, 392, 1, rotation=0),
            Beam(2217, 513, 1, rotation=0),
            Beam(2055, 352, 1, rotation=0),
            Beam(2214, 353, 1, rotation=0),
            Beam(2055, 312, 1, rotation=0),
            Beam(2054, 273, 1, rotation=0),
            Beam(1897, 272, 1, rotation=0),
            Beam(1738, 272, 1, rotation=0),
            Beam(1736, 232, 1, rotation=0),
            Beam(1736, 191, 1, rotation=0),
            Beam(1735, 151, 1, rotation=0),
            Beam(1735, 111, 1, rotation=0),
            Beam(1893, 111, 1, rotation=0),
            Beam(2053, 111, 1, rotation=0),
            Beam(2615, 352, 1, rotation=0),
            Beam(2988, 335, 1, rotation=0),
            Beam(3352, 360, 1, rotation=0),
            Beam(3731, 481, 1, rotation=0),
            Beam(4049, 646, 1, rotation=0),
            Beam(4207, 647, 1, rotation=0),
            Beam(4366, 646, 1, rotation=0),
            Beam(3058, 867, 1, rotation=1),
            Beam(3056, 710, 1, rotation=1),
            Beam(595, 1231, 1, rotation=0),
            Beam(975, 1132, 1, rotation=0),
            Beam(1281, 1018, 1, rotation=0),
            Beam(2533, 352, 1, rotation=0),
            Beam(2926, 335, 1, rotation=0),
            Beam(3309, 359, 1, rotation=0),
            Beam(3660, 480, 1, rotation=0),
        ],
        'coins': [
            Coin(3780, 432),
            Coin(758, 1187),
            Coin(1105, 1090),
            Coin(1413, 937),
            Coin(2116, 1161),
            Coin(2331, 939),
            Coin(2277, 775),
            Coin(3403, 315),
            Coin(660, 1188),
            Coin(1913, 235),
            Coin(1913, 192),
            Coin(1983, 192),
            Coin(1986, 236),
        ],
        'beams2': [
            Beam2(2071, 1053, rotation=2),
            Beam2(2111, 1053, rotation=2),
            Beam2(2151, 1053, rotation=2),
            Beam2(2191, 1053, rotation=2),
        ],
        'ghosts': [
            Ghost(2557, 745),
        ],
        'serce': [
            Serce(2244, 574),
        ],
        'door': Door(4416, 446),

        'background': Camera(),

    }


def level_9():
    return {
        'nb_level': 9,
        'beams': [
            Beam(1, 905, 1, rotation=0),
            Beam(159, 905, 1, rotation=0),
            Beam(316, 905, 1, rotation=0),
            Beam(475, 904, 1, rotation=0),
            Beam(741, 1011, 1, rotation=0),
            Beam(1042, 946, 1, rotation=0),
            Beam(1323, 862, 1, rotation=0),
            Beam(1623, 835, 1, rotation=0),
            Beam(1883, 923, 1, rotation=0),
            Beam(2113, 994, 1, rotation=0),
            Beam(2354, 1070, 1, rotation=0),
            Beam(2631, 1077, 1, rotation=0),
            Beam(2914, 1080, 1, rotation=0),
            Beam(3073, 1081, 1, rotation=0),
            Beam(3231, 1080, 1, rotation=0),
            Beam(3390, 1080, 1, rotation=0),
            Beam(3547, 1080, 1, rotation=0),
            Beam(3703, 1079, 1, rotation=0),
            Beam(3861, 1078, 1, rotation=0),
            Beam(4020, 1079, 1, rotation=0),
            Beam(2875, 1080, 1, rotation=1),
            Beam(2875, 1119, 1, rotation=1),
            Beam(2914, 1238, 1, rotation=0),
            Beam(3071, 1239, 1, rotation=0),
            Beam(3230, 1239, 1, rotation=0),
            Beam(3388, 1240, 1, rotation=0),
            Beam(3547, 1241, 1, rotation=0),
            Beam(3705, 1241, 1, rotation=0),
            Beam(3863, 1242, 1, rotation=0),
            Beam(4022, 1242, 1, rotation=0),
            Beam(4021, 1040, 1, rotation=0),
            Beam(4372, 989, 1, rotation=0),
            Beam(4372, 1029, 1, rotation=0),
            Beam(4661, 933, 1, rotation=0),
            Beam(4661, 972, 1, rotation=0),
            Beam(4883, 877, 1, rotation=0),
            Beam(4883, 918, 1, rotation=0),
            Beam(4848, 1130, 1, rotation=0),
            Beam(4800, 1129, 1, rotation=0),
            Beam(4632, 1285, 1, rotation=0),
            Beam(4236, 1372, 1, rotation=0),
            Beam(4340, 1191, 1, rotation=0),
            Beam(4832, 1531, 1, rotation=0),
            Beam(4653, 1683, 1, rotation=0),
            Beam(4395, 1687, 1, rotation=0),
            Beam(4141, 1690, 1, rotation=0),
            Beam(3914, 1690, 1, rotation=0),
            Beam(3754, 1690, 1, rotation=0),
            Beam(3595, 1690, 1, rotation=0),
            Beam(3851, 1690, 1, rotation=0),
            Beam(3437, 1690, 1, rotation=0),
            Beam(3279, 1690, 1, rotation=0),
            Beam(3120, 1690, 1, rotation=0),
            Beam(2961, 1690, 1, rotation=0),
        ],
        'coins': [
            Coin(1100, 895),
            Coin(1677, 789),
            Coin(2159, 949),
            Coin(2949, 1187),
            Coin(3084, 1186),
            Coin(3230, 1187),
            Coin(3379, 1189),
            Coin(3518, 1188),
            Coin(3664, 1188),
            Coin(3819, 1190),
            Coin(3981, 1186),
            Coin(4926, 834),
            Coin(3735, 1646),
            Coin(3509, 1644),
            Coin(3289, 1639),
        ],
        'beams2': [
            Beam2(3421, 1671, rotation=0),
            Beam2(3624, 1670, rotation=0),
            Beam2(3832, 1673, rotation=0),
            Beam2(3199, 1671, rotation=0),
        ],
        'ghosts': [
        ],
        'serce': [
            Serce(4074, 1151),
        ],
        'door': Door(2978, 1489),
        "background": Camera(),
    }


class Game:
    def __init__(self, player):
        self.levels = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9]
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

    def load_level(self, level: dict):
        self.current_level = level["nb_level"]
        self.beams = level['beams']
        self.beams2 = level['beams2']
        self.coins = level['coins']
        self.ghosts = level['ghosts']
        self.door = level['door']
        self.camera = level['background']
        self.serca = level['serce']  # hearts

    def run(self):
        run = True
        pause = False

        clock = pygame.time.Clock()
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

        self.resume(self.current_level)

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

    def resume(self, current_level):
        run = True
        clock = pygame.time.Clock()
        background = pygame.image.load('Sprites/main menu/menu_background.png').convert_alpha()

        self.player.x_cord = 0
        self.player.y_cord = 0

        # reset player if it died
        if not self.player.alive:
            self.player.health = 100
            self.player.alive = True

        play_button = Button(515, 500, "Sprites/next_level/next")
        shop_button = Button(900, 500, "Sprites/next_level/next")
        menu_button = Button(100, 500, "Sprites/next_level/next")

        font = pygame.font.SysFont('None', 100)
        text = font.render('Game Over', True, RED)
        while run:
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            if play_button.tick():
                self.load_level(self.levels[current_level - 1]())
                self.run()
                run = False

            if menu_button.tick():
                run = False
                self.menu_level()

            if shop_button.tick():
                run = False
                self.shop(self.score, current_level)

            window.blit(background, (0, 0))
            window.blit(text, (400, 300))
            play_button.draw(window)
            shop_button.draw(window)
            menu_button.draw(window)

            pygame.display.flip()

    def menu_level(self):
        n = len(self.levels)
        run = True
        clock = pygame.time.Clock()
        background = pygame.image.load('Sprites/main menu/menu_background.png').convert_alpha()

        level_buttons = []
        font = pygame.font.SysFont('None', 50)
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

    def shop(self, score, level):
        run = True
        clock = 0
        text = Text(950, 10)
        background = pygame.image.load('Sprites/main menu/menu_background.png')
        postacie = ['John', 'Jan']
        active = [True, False]
        price = [0, 2]
        shop_button = Button(100, 100, "Sprites/next_level/next")
        active_button = Button(100, 350, "Sprites/active")
        lock_button = Button(100, 350, "Sprites/lock")
        buy_button = Button(800, 350, "Sprites/buy")
        left = Button(50, 500, "Sprites/strzalka")
        i = 0
        right = Button(1000, 500, "Sprites/strzalkapr")
        while run:
            clock += pygame.time.Clock().tick(60) / 1000  # maksymalnie 60 fps
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
                    run = False

            if shop_button.tick():
                self.resume(level)
            if active_button.tick() and active[i]:
                player = Player(postacie[i])
            if buy_button.tick() and score - price[i] >= 0:
                score -= price[i]
                price[i] = 0
                active[i] = True

            if left.tick():
                if i > 0:
                    i -= 1
            if right.tick():
                if i < len(postacie) - 1:
                    i += 1

            window.blit(background, (0, 0))

            pygame.draw.rect(window, [200, 200, 200],
                             pygame.Rect(360, 300, 400, 400))
            window.blit(pygame.image.load(f'Sprites/{postacie[i]}/stand.png'),
                        (560, 500))
            shop_button.draw(window)
            left.draw(window)
            right.draw(window)
            if active[i]:
                active_button.draw(window)
            else:
                lock_button.draw(window)

            buy_button.draw(window)
            text.draw(window, score)

            pygame.display.update()


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
