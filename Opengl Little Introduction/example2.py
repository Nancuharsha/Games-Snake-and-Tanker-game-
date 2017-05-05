import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

Screen = pygame.display.set_mode((800,600))
Screen.fill(blue)

pix = pygame.PixelArray(Screen)

pix[20][20] = green

pygame.draw.line(Screen,red,(300,400),(600,500),5)

pygame.draw.circle(Screen,red,(300,400),40)

pygame.draw.rect(Screen,green,(200,200,30,30))

pygame.draw.polygon(Screen,white,((10,100),(15,120),(202,203))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
