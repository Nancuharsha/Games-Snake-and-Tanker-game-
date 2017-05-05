import pygame , sys ,time, random
pygame.init()

red = (200,0,0)
light_red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,200,0)
light_green = (0,255,0)
yellow = (200,200,0)
light_yellow = (250,250,0)
Display_width = 800
Display_height = 600
ScreenDisplay = pygame.display.set_mode((Display_width,Display_height),0,32)
pygame.display.set_caption('Tanker')
clock = pygame.time.Clock()

FPS = 10

smallfont = pygame.font.SysFont("comicansms",25)
medfont = pygame.font.SysFont("comicansms",50)
largefont = pygame.font.SysFont("comicansms",100)

def cube(startpoint,fullsize):
    node_1 = [startpoint[0],startpoint[1]]
    node_2 = [startpoint[0]+fullsize,startpoint[1]]
    node_3 = [startpoint[0],startpoint[1]+fullsize]
    node_4 = [startpoint[0]+fullsize,startpoint[1]+fullsize]

    offset = int(fullsize/2)
    x_mid = int(Display_width/2)
    x_offset = startpoint[0] - x_mid
    if x_offset > 100 or x_offset < -100:
        x_offset = 100
        
    

    y_mid = int(Display_height/2)
    y_offset = startpoint[1] - y_mid
    if y_offset > 100 or y_offset < -100:
        y_offset = 100
        

    node_5 = [node_1[0]+x_offset,node_1[1]-y_offset]
    node_6 = [node_2[0]+x_offset,node_2[1]-y_offset]
    node_7 = [node_3[0]+x_offset,node_3[1]-y_offset]
    node_8 = [node_4[0]+x_offset,node_4[1]-y_offset]



    pygame.draw.line(ScreenDisplay,white,(node_1),(node_2))
    pygame.draw.line(ScreenDisplay,white,(node_3),(node_4))
    pygame.draw.line(ScreenDisplay,white,(node_1),(node_3))
    pygame.draw.line(ScreenDisplay,white,(node_2),(node_4))

    pygame.draw.line(ScreenDisplay,white,(node_5),(node_6))
    pygame.draw.line(ScreenDisplay,white,(node_5),(node_7))
    pygame.draw.line(ScreenDisplay,white,(node_7),(node_8))
    pygame.draw.line(ScreenDisplay,white,(node_6),(node_8))

    
    pygame.draw.line(ScreenDisplay,white,(node_1),(node_5))
    pygame.draw.line(ScreenDisplay,white,(node_2),(node_6))
    pygame.draw.line(ScreenDisplay,white,(node_3),(node_7))
    pygame.draw.line(ScreenDisplay,white,(node_4),(node_8))

    pygame.draw.circle(ScreenDisplay,light_green,node_1,5)
    pygame.draw.circle(ScreenDisplay,light_green,node_2,5)
    pygame.draw.circle(ScreenDisplay,light_green,node_3,5)
    pygame.draw.circle(ScreenDisplay,light_green,node_4,5)

    pygame.draw.circle(ScreenDisplay,light_green,node_5,5)
    pygame.draw.circle(ScreenDisplay,light_green,node_6,5)
    pygame.draw.circle(ScreenDisplay,light_green,node_7,5)
    pygame.draw.circle(ScreenDisplay,light_green,node_8,5)




    
def gameLoop():
    location = [300,300]
    size = 200
    change = 0
    z_move = 0
    z_position = 1
    y_move = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change = -5
                elif event.key == pygame.K_RIGHT:
                    change = 5
                elif event.key == pygame.K_UP:
                    y_move = -5 
                    #change = -1
                elif event.key == pygame.K_DOWN:
                    y_move = 5
                    #change = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT :
                    change = 0
                elif event.key == pygame.K_RIGHT:
                    change = 0
                elif event.key == pygame.K_UP:
                    y_move = 0
                    #change = 0
                elif event.key == pygame.K_DOWN:
                    y_move = 0
                    #change = 0
        ScreenDisplay.fill(black)
        if z_position > 200:
            z_move = 0
        z_position += z_move
        #current_size = int(size/(z_position*0.1))

        current_size = size
        #size += change
        location[0] += change
        location[1] += y_move
        cube(location,current_size)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

gameLoop()
