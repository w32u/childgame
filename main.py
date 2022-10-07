import sys, pygame
pygame.init()
pygame.display.set_caption('childgame')

size = width, height = 640, 480
screen_color = (0,0,0)
circle_color = (255,255,255)
pressed = False

screen = pygame.display.set_mode(size)

def getPos():
    pos = pygame.mouse.get_pos()
    return pos

def drawCircle():
    pos=getPos()
    pygame.draw.circle(screen, circle_color, pos, 20)

def main():
    global size, screen_color, circle_color, pressed, screen
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if pygame.mouse.get_pressed()[0]:
                try:
                    pressed = True
                except AttributeError:
                    pass
            else:
                pressed = False
        
        pygame.display.update()
        
        screen.fill(screen_color)
        if pressed:
            drawCircle()
        
        pygame.display.flip()


if __name__ == '__main__':
    main()