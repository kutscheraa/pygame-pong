import pygame

pygame.init()

win = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong - MARTIN KUCERA')

bila = (255, 255, 255)
cerna = (0, 0, 0)
#bg =

class Palka(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(bila)
        self.rect = self.image.get_rect()
        self.points = 0

class Micek(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(bila)
        self.rect = self.image.get_rect()
        self.speed = 6.5
        self.dx = 1
        self.dy = 1

palka1 = Palka()
palka1.rect.x = 25
palka1.rect.y = 225

palka2 = Palka()
palka2.rect.x = 715
palka2.rect.y = 225

palka_speed = 5

micek = Micek()
micek.rect.x = 375
micek.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(palka1, palka2, micek)

def redraw():

    win.fill(cerna)

    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('UJEP', False, bila)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    win.blit(text, textRect)

    # Hrac 1
    p1_score = font.render(str(palka1.points), False, bila)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    # Hrac 2
    p2_score = font.render(str(palka2.points), False, bila)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)

    all_sprites.draw(win)

    pygame.display.update()


pustit = True

while pustit:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pustit = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        palka1.rect.y += - palka_speed
    if key[pygame.K_s]:
        palka1.rect.y += + palka_speed
    if key[pygame.K_UP]:
        palka2.rect.y += - palka_speed
    if key[pygame.K_DOWN]:
        palka2.rect.y += + palka_speed

    micek.rect.x += micek.speed * micek.dx
    micek.rect.y += micek.speed * micek.dy

    if micek.rect.y > 500:
        micek.dy = -1

    if micek.rect.x > 750:
        micek.rect.x, micek.rect.y = 375, 250
        micek.dx = -1
        palka1.points += 1

    if micek.rect.y < 0:
        micek.dy = 1

    if micek.rect.x < 0:
        micek.rect.x, micek.rect.y = 375, 250
        micek.dx = 1
        palka2.points += 1

    if palka1.rect.colliderect(micek.rect):
        micek.dx = 1

    if palka2.rect.colliderect(micek.rect):
        micek.dx = -1

    redraw()

pygame.quit()

