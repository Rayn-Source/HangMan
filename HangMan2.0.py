import pygame,random, sys
pygame.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.Font(None, 40)
word = random.choice(['python', 'pygame', 'hangman'])
guessed, wrong = ['_'] * len(word), []
attempts = 6

def draw_hangman(strikes):
    parts = [(150, 400, 150, 150), (100, 400, 200, 400), (150, 150, 250, 150), (250, 150, 250, 200),
             (250, 225, 25), (250, 250, 250, 320), (250, 270, 220, 320), (250, 270, 280, 320),
             (250, 320, 220, 380), (250, 320, 280, 380)]
    for i in range(strikes): pygame.draw.line(screen, (0, 0, 0), parts[i][:2], parts[i][2:], 5) if i != 8 else pygame.draw.circle(screen, (0, 0, 0), parts[i][:2], parts[i][2], 5)

while attempts > 0 and '_' in guessed:
    screen.fill((255, 255, 255))
    screen.blit(font.render(' '.join(guessed), True, (0, 0, 0)), (100, 100))
    screen.blit(font.render('Wrong: ' + ' '.join(wrong), True, (255, 0, 0)), (100, 400))
    draw_hangman(6 - attempts)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            guess = chr(event.key)
            if guess in word and guess not in guessed:
                for i, letter in enumerate(word):
                    if letter == guess: guessed[i] = guess
            elif guess not in wrong: wrong.append(guess); attempts -= 1

screen.fill((255, 255, 255))
screen.blit(font.render('You Win!' if '_' not in guessed else 'You Lose!', True, (255, 0, 0)), (150, 200))
pygame.display.flip()
pygame.time.wait(2000)