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

Display_width = 1000
Display_height = 800



tankWidth =  40
tankHeight = 20

ground_height = 35

turrentWidth = 5
wheelWidth = 5

ScreenDisplay = pygame.display.set_mode((Display_width,Display_height),0,32)

pygame.display.set_caption('Tanker')
clock = pygame.time.Clock()
appleThick = 20
Block_size = 20
FPS = 10

smallfont = pygame.font.SysFont("comicansms",25)
medfont = pygame.font.SysFont("comicansms",50)
largefont = pygame.font.SysFont("comicansms",100)


def text_objects(text , color, size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg,color, buttonx,buttony,buttonwidth,buttonheigth,size="small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = (buttonx+(buttonwidth/2)),buttony+(buttonheigth/2)
    ScreenDisplay.blit(textSurf,textRect)

def message_to_text(msg,color,y_display = 0,size = "small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = (Display_width/2),(Display_height/2) + y_display
    ScreenDisplay.blit(textSurf,textRect)


def game_controls():
            intro = True
            while intro:
                ScreenDisplay.fill(white)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                message_to_text("Controls",
                                green,
                                -100,
                                "large")
                message_to_text("Fire : SpaceBar",red ,-30)
                message_to_text("Move turrent : up and  down",red ,0)
                message_to_text("Move Tank : Right and Left",red ,30)
                message_to_text("p to pause",red ,60,)

                

                button("play",100,500,100,50,green,light_green,"play")
                #button("Mainn",450,500,100,50,red,light_red,"mains")
                button("quit",800,500,100,50,yellow,light_yellow,"quit")

                
                pygame.display.update()
                clock.tick(10)


def tank(x,y,turpos):
    x = int(x)
    y = int(y)
    possibleTurrents = [(x-27,y-2),
                        (x-26,y-5),
                        (x-25,y-8),
                        (x-23,y-12),
                        (x-20,y-14),
                        (x-18,y-15),
                        (x-15,y-17),
                        (x-13,y-19),
                        (x-11,y-21),
                        
                        
                        ]
    
    pygame.draw.circle(ScreenDisplay,black,(x,y),int(tankHeight/2))
    pygame.draw.rect(ScreenDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(ScreenDisplay,black,(x,y),possibleTurrents[turpos],turrentWidth)

    pygame.draw.circle(ScreenDisplay,black,(x-15,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x-10,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x-5,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x+5,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x+10,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x+15,y+20),wheelWidth)
    return possibleTurrents[turpos]

def enemy_tank(x,y,turpos):
    x = int(x)
    y = int(y)
    possibleTurrents = [(x+27,y-2),
                        (x+26,y-5),
                        (x+25,y-8),
                        (x+23,y-12),
                        (x+20,y-14),
                        (x+18,y-15),
                        (x+15,y-17),
                        (x+13,y-19),
                        (x+11,y-21),
                        
                        
                        ]
    
    pygame.draw.circle(ScreenDisplay,black,(x,y),int(tankHeight/2))
    pygame.draw.rect(ScreenDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(ScreenDisplay,black,(x,y),possibleTurrents[turpos],turrentWidth)

    pygame.draw.circle(ScreenDisplay,black,(x-15,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x-10,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x-5,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x+5,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x+10,y+20),wheelWidth)
    pygame.draw.circle(ScreenDisplay,black,(x+15,y+20),wheelWidth)
    return possibleTurrents[turpos]


def game_intro():
    intro = True
    while intro:
        ScreenDisplay.fill(white)
        message_to_text("Welcome to Tannker",
                        green,
                        -100,
                        "large")
        message_to_text("objective shoot and destroy the Enemy tanker",red ,-30)
        message_to_text("Before they kill you",red )
        message_to_text("More enemies destroy they get harder",red ,30)
        #message_to_text(" play press c or quit press Q or exit button and p to pause",red ,100,"medium")

        

        button("play",100,500,100,50,green,light_green,"play")
        button("control",450,500,100,50,red,light_red,"controls")
        button("quit",800,500,100,50,yellow,light_yellow,"quit")

        
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


def Score(score):
    tex = smallfont.render("SCORE: "+str(score),True , black)
    ScreenDisplay.blit(tex,[0,0])

def button(text,x,y,width,height,inactive_color,active_color,action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    
    if x+width > cur[0] > x and y+height > cur[1] > y:
        pygame.draw.rect(ScreenDisplay,active_color,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "mains":
                game_intro()
                
    else:
        pygame.draw.rect(ScreenDisplay,inactive_color,(x,y,width,height))

    text_to_button(text,black,x,y,width,height)
def power(level):
    text = smallfont.render("Power:"+str(level)+"%",True,black)
    ScreenDisplay.blit(text,[Display_width/2,0])

def barrier(xlocation,randomHeight,barrier_width):

    pygame.draw.rect(ScreenDisplay,black,[xlocation,Display_height-randomHeight,barrier_width,randomHeight])

def explosion(hitx,hity,size = 50):
    pygame.mixer.music.load("bomb2.mp3")
    pygame.mixer.music.play(1)
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = hitx,hity

        colorChoices = [green,light_green,yellow,light_yellow]

        magnitude = 1

        while magnitude < size:
            exploding_bit_x = hitx+ random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = hity+ random.randrange(-1*magnitude,magnitude)
            pygame.draw.circle(ScreenDisplay,colorChoices[random.randrange(0,4)],(exploding_bit_x,exploding_bit_y),4)
            magnitude += 1
            pygame.display.update()
            clock.tick(100)
        explode = False
        

def fireShell(gun,tankx,tanky,turpos,gum_power,xlocation,barrier_width,randomHeight,enemyTankx,enemyTanky):
    fire = True
    damage = 0
    pygame.mixer.music.load("bomb.mp3")
    pygame.mixer.music.play(1)
    print enemyTankx,"hello in fireshell"
    startingShell = list(gun)
    #print("Fire")
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(ScreenDisplay,green,(startingShell[0],startingShell[1]),5)
        
        startingShell[0] -= (12 - turpos)**2
        startingShell[1] += int((((startingShell[0]-gun[0])*0.015/(gum_power/50))**2)-(turpos + turpos/(12-turpos)))
        if startingShell[1] > Display_height-ground_height:

            hit_x = int((startingShell[0] * (Display_height-ground_height))/startingShell[1])
            hit_y = int(Display_height-ground_height)
            if enemyTankx + 10 > hit_x >enemyTankx - 10:
                damage = 25
            elif enemyTankx + 15 > hit_x >enemyTankx - 15:
                damage = 18
            elif enemyTankx + 25 > hit_x >enemyTankx - 25:
                damage = 10
            elif enemyTankx + 35 > hit_x >enemyTankx - 35:
                damage = 5
##                for i in range(25):
##                    print "oh! shit"
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <=Display_height
        check_y_2 = startingShell[1] >=Display_height -randomHeight
        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int((startingShell[0] ))
            hit_y = int(startingShell[1])
            explosion(hit_x,hit_y)
            fire = False
            

        
        pygame.display.update()
        clock.tick(100)
    return damage


def e_fireShell(gun,tankx,tanky,turpos,gum_power,xlocation,barrier_width,randomHeight,ptankx,ptanky):
    currentpower = 1
    damage = 0
    pygame.mixer.music.load("bomb.mp3")
    pygame.mixer.music.play(-1)
    power_found = False

    while not power_found:
        currentpower += 1

        if currentpower > 150:
            power_found = True
        fire = True

        startingShell = list(gun)
        #print("Fire")
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
##            pygame.draw.circle(ScreenDisplay,green,(startingShell[0],startingShell[1]),5)
            
            startingShell[0] += (12 - turpos)**2
            
            startingShell[1] += int((((startingShell[0]-gun[0])*0.015/(currentpower/50.0))**2)-(turpos + turpos/(12-turpos)))
            if startingShell[1] > Display_height-ground_height:

                hit_x = int((startingShell[0] * (Display_height-ground_height))/startingShell[1])
                hit_y = int(Display_height-ground_height)
##                explosion(hit_x,hit_y)
                if ptankx + 15 >hit_x >ptankx-15:
                    power_found = True
                    
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <=Display_height
            check_y_2 = startingShell[1] >=Display_height -randomHeight
            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0] ))
                hit_y = int(startingShell[1])
##                explosion(hit_x,hit_y)
                fire = False

    fire = True

    startingShell = list(gun)
    print("Fire")
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(ScreenDisplay,green,(startingShell[0],startingShell[1]),5)
        
        startingShell[0] += (12 - turpos)**2
        
        currentpower = random.randrange(int(currentpower*0.95),int(currentpower*1.05))
        startingShell[1] += int((((startingShell[0]-gun[0])*0.015/(currentpower/50.0))**2)-(turpos + turpos/(12-turpos)))
        if startingShell[1] > Display_height-ground_height:

            hit_x = int((startingShell[0] * (Display_height-ground_height))/startingShell[1])
            hit_y = int(Display_height-ground_height)
            if ptankx + 10 > hit_x > ptankx - 10:
                damage = 25
            elif ptankx + 15 > hit_x > ptankx - 15:
                damage = 18
            elif ptankx + 25 > hit_x > ptankx - 25:
                damage = 10
            elif ptankx + 35 > hit_x > ptankx - 35:
                damage = 5
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <=Display_height
        check_y_2 = startingShell[1] >=Display_height -randomHeight
        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int((startingShell[0] ))
            hit_y = int(startingShell[1])
            explosion(hit_x,hit_y)
            fire = False
            

        
        pygame.display.update()
        clock.tick(100)
    return damage


def you_win():
    win = True
    while win:
        ScreenDisplay.fill(white)
        message_to_text("Game over",
                        green,
                        -100,
                        "large")
        message_to_text("You win!congo",red ,-30)
 

        button("play Again",100,500,150,50,green,light_green,"play")
        button("control",450,500,100,50,red,light_red,"controls")
        button("quit",800,500,100,50,yellow,light_yellow,"quit")

        
        pygame.display.update()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



def game_over():
    over = True
    while over:
        ScreenDisplay.fill(white)
        message_to_text("Game over",
                        green,
                        -100,
                        "large")
        message_to_text("You died",red ,-30)
 

        button("play Again",100,500,150,50,green,light_green,"play")
        button("control",450,500,100,50,red,light_red,"controls")
        button("quit",800,500,100,50,yellow,light_yellow,"quit")

        
        pygame.display.update()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


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


        pygame.display.update()

def health_bar(player_health,enemy_health):
    if player_health > 75 :
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else :
        player_health_color = red
    if enemy_health > 75 :
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else :
        enemy_health_color = red
    pygame.draw.rect(ScreenDisplay,player_health_color,(680,25,player_health,25))
    pygame.draw.rect(ScreenDisplay,enemy_health_color,(20,25,enemy_health,25))
        
def gameLoop():


    gameExit = False
    gameOver = False

    mainTankX = Display_width*0.9
    mainTanky = Display_height*0.9
    tankMove =0
    player_health = 100
    enemy_health = 100

    currentTurpos = 0
    changeTur = 0
    barrier_width = 50

    enemyTankX = Display_width*0.1
    enemyTankY = Display_height*0.9



    
    firepower = 50
    power_change = 0

    xlocation = Display_width/2 +random.randint(-0.1*Display_width,0.1*Display_width)
    randomHeight = random.randrange(Display_height*0.1,Display_height*0.5)

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
                
                gameExit = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5 

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                elif event.key == pygame.K_p:
                    Pause()
                elif event.key == pygame.K_SPACE:
                    damage1 = fireShell(gun,mainTankX,mainTanky,currentTurpos,firepower,xlocation,barrier_width,randomHeight,enemyTankX,enemyTankY)
                    print damage1,enemyTankX ,"helllo in if gameloop"
                    enemy_health -= damage1
                    possibleMovement = ['f','r']
                    moveIndex = random.randrange(0,2)
                    for x in range(random.randrange(0,10)):
                        if Display_width*0.3 >enemyTankX> Display_width*0.03:
                            if possibleMovement[moveIndex] == "f":
                                enemyTankX += 5
                            if possibleMovement[moveIndex] == "r":
                                enemyTankX -= 5
                            ScreenDisplay.fill(white)
                            health_bar(player_health,enemy_health)
                            gun = tank(mainTankX,mainTanky,currentTurpos)
                            enemy_gun = enemy_tank(enemyTankX,enemyTankY,8)

                            firepower += power_change
                            power(firepower)
                                    
                            barrier(xlocation,randomHeight,barrier_width)
                            ScreenDisplay.fill(green,rect = [0,Display_height-ground_height,Display_width,ground_height])
                                
                            pygame.display.update()
                            clock.tick(FPS)
                                    
                                
                    damage =e_fireShell(enemy_gun,enemyTankX,enemyTankY,currentTurpos,firepower,xlocation,barrier_width,randomHeight,mainTankX,mainTanky)
                    print damage

                    player_health -= damage
                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1

            elif event.type == pygame.KEYUP:
                

                if event.key == pygame.K_LEFT :
                    tankMove = 0
                if event.key == pygame.K_RIGHT:
                    tankMove = 0 

                if event.key == pygame.K_UP:
                    changeTur = 0

                if event.key == pygame.K_DOWN:
                    changeTur = 0


                if event.key == pygame.K_a:
                    power_change = 0
                if event.key == pygame.K_d:
                    power_change = 0
                
                    



        mainTankX += tankMove
        currentTurpos += changeTur
        if currentTurpos >8:
            currentTurpos = 8
        elif currentTurpos <0:
            currentTurpos = 0

        if mainTankX - (tankWidth/2) < xlocation + barrier_width:
            mainTankX += 5

        ScreenDisplay.fill(white)
        health_bar(player_health,enemy_health)
        gun = tank(mainTankX,mainTanky,currentTurpos)
        enemy_gun = enemy_tank(enemyTankX,enemyTankY,8)

        firepower += power_change
        if firepower > 200:
            firepower = 200
        elif firepower <50:
            firepower = 50
        
        power(firepower)
        
        barrier(xlocation,randomHeight,barrier_width)
        ScreenDisplay.fill(green,rect = [0,Display_height-ground_height,Display_width,ground_height])
    
        pygame.display.update()
        
        if enemy_health < 1:
            you_win()
        elif player_health < 1:
            game_over()

            


        clock.tick(FPS)

    pygame.quit()


    quit()


##game_over()
game_intro()
gameLoop()

