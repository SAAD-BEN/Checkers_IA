import pygame
from checkers.button import Button
from checkers.constants import WIDTH, HEIGHT, WHITE, BLACK, TITLE_FONT, BODY_FONT_SMALL, PADDING


buttons = [Button("START", "START", WIDTH / 2 + PADDING - 80, HEIGHT / 2 + PADDING * 2 + 150, BLACK, 0)]
def draw(win):
    win.fill(WHITE)

    text = TITLE_FONT.render("Checkers", 1, BLACK)
    win.blit(text, (round(WIDTH / 2) - round(text.get_width() / 2), 25))

    text = BODY_FONT_SMALL.render("v0.1", 1, BLACK)
    win.blit(text, (WIDTH - text.get_width() - PADDING, 150 - text.get_height() - PADDING))

    for b in buttons:
        b.draw(win)

    dices = pygame.image.load("assets/chinese-checkers-256.png")
    win.blit(dices,(WIDTH /2 -128,HEIGHT/2 -128))
    pygame.display.update()

def run(window):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.click(pos):
                        if b.button_id == 'START':
                            return 'INGAME'
        draw(window)
