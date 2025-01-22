import pygame
pygame.init()

def song():
    file = "sound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
fps = 60

timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = WHITE

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint!')
song()
painting = []

def draw_menu(size, color):
    pygame.draw.rect(screen, GRAY, [0, 0, WIDTH, 70])
    pygame.draw.line(screen, BLACK, (0,70), (WIDTH,70), 3)
    xl_brush = pygame.draw.rect(screen, BLACK, [10, 10, 50, 50])
    pygame.draw.circle(screen, 
                       WHITE, (35, 35), 20)
    l_brush = pygame.draw.rect(screen, BLACK, [70, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (95, 35), 15)
    m_brush = pygame.draw.rect(screen, BLACK, [130, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (155, 35), 10)
    s_brush = pygame.draw.rect(screen, BLACK, [190, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    if size == 20:
        pygame.draw.rect(screen, 'green', [10, 10, 50, 50], 3)
    elif size == 15:
        pygame.draw.rect(screen, 'green', [70, 10, 50, 50], 3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', [130, 10, 50, 50], 3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', [190, 10, 50, 50], 3)

    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH -35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH -35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH -60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH -60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH -85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH -85, 35, 25, 25])
    white = pygame.draw.rect(screen, (0, 0, 0), [WIDTH -110, 10, 25, 25])
    black = pygame.draw.rect(screen, (255, 255, 255), [WIDTH -110, 35, 25, 25])
    color_rect = [blue, red, green,yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]
    return brush_list, color_rect, rgb_list
    

    

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

run = True
while run:
    timer.tick(fps)
    screen.fill(WHITE)
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))

    draw_painting(painting)

    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)

    brushes, colors, rgbs = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i*5)
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
        
    pygame.display.update()
pygame.quit()
