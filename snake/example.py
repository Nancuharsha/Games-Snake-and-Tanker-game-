import pygame , sys ,time, random
#from pygame.locals import *

pygame.init()

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

Display_width = 1000
Display_height = 800


ScreenDisplay = pygame.display.set_mode((Display_width,Display_height),0,32)

pygame.display.set_caption('MYEMYG(More_You_Eat_More_You_Grow)')
icon = pygame.image.load('kill.jpg')
pygame.display.set_icon(icon)
#pygame.display.update()
img = pygame.image.load('snakeHead.png')
appleimg = pygame.image.load('apple.png')
clock = pygame.time.Clock()
appleThick = 20
Block_size = 20
FPS = 10
direction = "right"
#font = pygame.font.SysFont(None, 25)
smallfont = pygame.font.SysFont("comicansms",25)
medfont = pygame.font.SysFont("comicansms",50)
largefont = pygame.font.SysFont("comicansms",100)



def Snake(Block_size,snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img , 270)
    if direction == "left":
        head = pygame.transform.rotate(img , 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img , 180)

    ScreenDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(ScreenDisplay, green , [XnY[0],XnY[1],Block_size,Block_size])

def text_objects(text , color, size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()



def message_to_text(msg,color,y_display = 0,size = "small"):
    textSurf,textRect = text_objects(msg,color,size)
##    screen_text = font.render(msg,True,color)
##    ScreenDisplay.blit(screen_text,[Display_width/2,Display_height/2])
    textRect.center = (Display_width/2),(Display_height/2) + y_display
    ScreenDisplay.blit(textSurf,textRect)

def game_intro():
    intro = True
    while intro:
        ScreenDisplay.fill(white)
        message_to_text("Welcome to MYEMYG",
                        green,
                        -100,
                        "large")
        message_to_text("objective of the game is to eat the red apple",red ,-30)
        message_to_text("more apples you eat more you grow",red )
        message_to_text("if you run into your self or the edges , you die",red ,30)
        message_to_text("If you want to play press c or if you want to quit press Q or exit button and p to pause",red ,100,"medium")
        pygame.display.update()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #time.sleep(1)
##        for event in pygame.event.get():
##
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_KP_ENTER:
##                    intro = False
##                    
##                if event.key == pygame.K_q:
##                    gameExit = True
##                    intro = False
##            if event.type == pygame.QUIT:
##                gameExit = True
##                intro = False



def Score(score):
    tex = smallfont.render("SCORE: "+str(score),True , black)
    ScreenDisplay.blit(tex,[0,0])

def Pause():
    pause = True
    message_to_text("Paused",black,-100,'large')
    message_to_text("press Q to Quit OR press C to Continue",black,0,'small')
    while pause:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #ScreenDisplay.fill(white)

        pygame.display.update()
        
def gameLoop():

    global direction
    direction = 'right'

    gameExit = False
    gameOver = False 

    lead_x = Display_width/2
    lead_y = Display_height/2

    lead_x_change = 20
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    
    randAppleX = round(random.randrange(0,Display_width-appleThick))#/10.0)*10.0
    randAppleY = round(random.randrange(0,Display_height-appleThick))#/10.0)*10.0

    while not gameExit:

        if gameOver == True:
            message_to_text("Game over",
                            red,
                            -50,
                            "large")
            message_to_text("press 'q' to Quit Or press 'c' to Play again",
                            red,
                            30,
                            "medium")
            
            

        while gameOver == True:
            #ScreenDisplay.fill(white)
           
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()
                        
                        
                    
            
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                #pygame.quit()
                #quit()
                gameExit = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -Block_size
                    lead_y_change = 0

                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = Block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -Block_size
                    lead_x_change = 0

                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = Block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    Pause()
                    


        if lead_x >= Display_width or lead_x < 0 or lead_y >= Display_height or lead_y < 0 :
            gameOver = True
            #if event.type == pygame.KEYUP:
             #   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              #      lead_x_change = 0
               # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #    lead_y_change = 0


        lead_x += lead_x_change
        lead_y += lead_y_change

        ScreenDisplay.fill(white)
        AppleSize = 20
        #pygame.draw.rect(ScreenDisplay , red , [randAppleX,randAppleY,AppleSize,AppleSize])
        ScreenDisplay.blit(appleimg,(randAppleX,randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]


        for each in snakeList[:-1]:
            if each == snakeHead:
                gameOver = True



        Snake(Block_size,snakeList)



        #pygame.draw.rect(ScreenDisplay, red , [300,300,10,30])

        Score(snakeLength-1)
        pygame.display.update()
            #print(event)
##        if lead_x ==randAppleX and lead_y ==randAppleY  :
##            randAppleX = round(random.randrange(0,Display_width-Block_size)/10.0)*10.0
##            randAppleY = round(random.randrange(0,Display_height-Block_size)/10.0)*10.0
##            snakeLength += 1
            #print("om nom nom")
##        if lead_x >= randAppleX and lead_x <= randAppleX+AppleSize:
##            if lead_y >= randAppleY and lead_y <= randAppleY+AppleSize:
##                randAppleX = round(random.randrange(0,Display_width-AppleSize))#/10.0)*10.0
##                randAppleY = round(random.randrange(0,Display_height-AppleSize))#/10.0)*10.0
##                snakeLength += 1
        if lead_x > randAppleX and lead_x < randAppleX+appleThick or lead_x +Block_size > randAppleX and lead_x + Block_size < randAppleX+appleThick:
            if lead_y > randAppleY and lead_y < randAppleY+appleThick or lead_y +Block_size > randAppleY and lead_y + Block_size < randAppleY+appleThick:
                randAppleX = round(random.randrange(0,Display_width-appleThick))#/10.0)*10.0
                randAppleY = round(random.randrange(0,Display_height-appleThick))#/10.0)*10.0
                snakeLength += 1
        clock.tick(FPS)
    #message_to_text("you lose",red)
    #pygame.display.update()

    #time.sleep(5)
    pygame.quit()


    quit()


game_intro()
gameLoop()
