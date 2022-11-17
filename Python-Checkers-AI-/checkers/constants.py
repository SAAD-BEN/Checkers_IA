import pygame

pygame.font.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

CROWN = pygame.transform.scale(pygame.image.load('assets/crown1.png'), (44, 25))

# fonts
# -----------------------------------------------------------------
TITLE_FONT = pygame.font.Font("assets/fonts/EncodeSans_black.ttf", 69)
SUB_TITLE_FONT = pygame.font.Font("assets/fonts/UniSansBook.otf", 36)
BODY_FONT = pygame.font.Font("assets/fonts/OpenSans_regular.ttf", 24)
BODY_FONT_SMALL = pygame.font.Font("assets/fonts/OpenSans_regular.ttf", 16)
BODY_FONT_EXTRA_SMALL = pygame.font.Font("assets/fonts/OpenSans_regular.ttf", 12)
BODY_FONT_BOLD = pygame.font.Font("assets/fonts/OpenSans_bold.ttf", 24)
GAME_OVER_FONT_BIG = pygame.font.Font("assets/fonts/game_over.ttf", 200)
GAME_OVER_FONT_SMALL = pygame.font.Font("assets/fonts/game_over.ttf", 30)

# colors
# -----------------------------------------------------------------
PURPLE = (51, 0, 111)
GOLD = (232, 211, 162)
METALLIC_GOLD = (124, 123, 76)
GRAY = (217, 217, 217)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  
BROWN = (102, 61, 20)
BLUE = (0, 0, 255)
GREY = (128,128,128)


# UI
# -----------------------------------------------------------------
PADDING = 8  # px
BIG_MARGIN = 48
WIDTH_INSIDE_MARGIN = WIDTH - BIG_MARGIN * 3
MIDDLE_X = round(WIDTH / 2)
# 0 is standard button, 1 is smaller. 2 is menu_item button. Each is in [width, height]
BUTTON_DIMENSIONS = [[150, 50],
                     [200, 33],
                     [round(WIDTH_INSIDE_MARGIN / 2) - PADDING * 2, 40],
                     [100, 33],
                     [10, 10]]
BUTTON_DEFAULT_FONT = [BODY_FONT_BOLD,
                       BODY_FONT_SMALL,
                       BODY_FONT_SMALL,
                       BODY_FONT_SMALL,
                       BODY_FONT_SMALL]
BUTTON_FONT_COLORS = [WHITE,
                      WHITE,
                      BLACK,
                      BLACK,
                      WHITE]

