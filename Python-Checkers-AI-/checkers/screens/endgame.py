import pygame
from checkers.button import Button
from checkers.constants import WIDTH, HEIGHT, WHITE, BLACK, RED, GAME_OVER_FONT_BIG, GAME_OVER_FONT_SMALL, PADDING
from checkers.game import Game


buttons = [Button("RESTART", "YES", WIDTH / 2 - 30, HEIGHT / 2 + PADDING + 65, RED, 4),
           Button("QUIT", "NO", WIDTH / 2 + 30, HEIGHT / 2 + PADDING + 65, RED, 4)]
def draw(win):
    win.fill(BLACK)

    text = GAME_OVER_FONT_BIG.render("Game Over", 1, RED)
    win.blit(text,((WIDTH /2) -(text.get_width()/2), (HEIGHT/2) -(text.get_height()/2)))

    game = Game(win)
    def winner():
        winnerColor = game.winner()
        if winnerColor == RED:
            return 'RED WON THE GAME'
        elif winnerColor == WHITE:
            return 'WHITE WON THE GAME'

    text = GAME_OVER_FONT_SMALL.render("DO YOU WANT TO RESTART?", 1, RED)
    win.blit(text,((WIDTH /2) -(text.get_width()/2), (HEIGHT/2) -(text.get_height()/2) + 60))


    for b in buttons:
        b.drawEnd(win)

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
                        if b.button_id == 'RESTART':
                            print("YES")
                            return 'INGAME'
                        if b.button_id == 'QUIT':
                            print("NO")
                            return 'QUIT'
        draw(window)
