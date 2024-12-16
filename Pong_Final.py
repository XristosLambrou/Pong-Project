import pygame
import sys
import random
import time
import Sound_Effects as SEF

pygame.init()

 
# -Παράμετροι Οθόνης-
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neo Pong")


#-Φορτώνουμε τις εικόνες-
GamePlayIMG = pygame.image.load('Image/landscape.png')
MAINMENUIMG = pygame.image.load('Image/fortress.png')
PLAYSUBMENUIMG = pygame.image.load('Image/gate.png')
SETTINGSSUBMENU = pygame.image.load('Image/desertnight.png')


#-Φορτώνουμε την μουσική-
SEF.Backround_Sound.play(-1)


# -Παράμετροι Παιχνιδιού-
DIFLEVEL = 0
MUSIC = True
SOUND = True
RTIMER = "10"
SOUND_STATUS = 1   #Καθορίζεται απο την μεταβλητή αν ο ήχος για τα Sound Effects θα είναι ανοιχτός 1 ή κλειστός 0
pygame.mouse.set_visible(False)


# -Γραμματοσειρές-
gamefont = pygame.font.SysFont("ArcadeClassic", 50)
credfont = pygame.font.SysFont("ArcadeClassic", 20)


# -Στοιχεία των μενού-
menu_items = ["Play","Settings","Quit"]
playsubmenu_items = ["Versus Player","Versus Computer","Return"]
setsubmenu_items = ["Hard Mode","Music","Sound Effects","Return"]

 
# -Function του κεντρικού μενού-
def main_menu():
    selected_item = 0
    while True:
        SCREEN.blit(MAINMENUIMG, (0, 0))
        title = gamefont.render("Neo Pong", True, WHITE)
        title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
        SCREEN.blit(title, title_rect)
        
        credits_title = credfont.render("Credits", True, WHITE)
        credits_title_rect = credits_title.get_rect(bottomright=(WIDTH - 20, HEIGHT - 110))
        SCREEN.blit(credits_title, credits_title_rect)
        
        n1 = credfont.render("Xristos Lamprou", True, (100, 100, 100))
        n1_rect = n1.get_rect(bottomright=(WIDTH - 20, HEIGHT - 80))
        SCREEN.blit(n1, n1_rect)
        
        n2 = credfont.render("Mavrikios Mavrikos", True, (100, 100, 100))
        n2_rect = n2.get_rect(bottomright=(WIDTH - 20, HEIGHT - 50))
        SCREEN.blit(n2, n2_rect)
        
        n3 = credfont.render("Spyros Linardos", True, (100, 100, 100))
        n3_rect = n3.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))
        SCREEN.blit(n3, n3_rect)

        controls_title = credfont.render("Controls", True, WHITE)
        controls_title_rect = controls_title.get_rect(bottomleft=(20,HEIGHT - 110))
        SCREEN.blit(controls_title, controls_title_rect)
        
        c1 = credfont.render("Menu Navigation   UP  AND  DOWN", True, (100, 100, 100))
        c1_rect = c1.get_rect(bottomleft=(20, HEIGHT - 80))
        SCREEN.blit(c1, c1_rect)
        
        c2 = credfont.render("Player 1   W  AND  S", True, (100, 100, 100))
        c2_rect = c2.get_rect(bottomleft=(20, HEIGHT - 50))
        SCREEN.blit(c2, c2_rect)
        
        c3 = credfont.render("Player 2   UP  AND  DOWN", True, (100, 100, 100))
        c3_rect = c3.get_rect(bottomleft=(20, HEIGHT - 20))
        SCREEN.blit(c3, c3_rect)
        
        for i, item in enumerate(menu_items):
            mitems = gamefont.render(item, True, WHITE if i == selected_item else (100, 100, 100))
            mitems_rect = mitems.get_rect(center=(WIDTH/2, HEIGHT/2 + i*50))
            SCREEN.blit(mitems, mitems_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected_item > 0:
                        selected_item -= 1
                elif event.key == pygame.K_DOWN:
                    if selected_item < len(menu_items) - 1:
                        selected_item += 1
                elif event.key == pygame.K_RETURN:
                    return selected_item


# -Function του υπομενού Play-
def playsubmenu():
    selected_item = 0
    while True:
        SCREEN.blit(PLAYSUBMENUIMG, (0, 0))
        title = gamefont.render("Choose Game Mode", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
        SCREEN.blit(title, title_rect)

        for i, item in enumerate(playsubmenu_items):
            pitems = gamefont.render(item, True, BLACK if i == selected_item else (100, 100, 100))
            pitems_rect = pitems.get_rect(center=(WIDTH/2, HEIGHT/2 + i*50))
            SCREEN.blit(pitems, pitems_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected_item > 0:
                        selected_item -= 1
                elif event.key == pygame.K_DOWN:
                    if selected_item < len(playsubmenu_items) - 1:
                        selected_item += 1
                elif event.key == pygame.K_RETURN:
                    return selected_item


# -Function του υπομενού Settings-
def setsubmenu():
    selected_item = 0
    while True:
        SCREEN.blit(SETTINGSSUBMENU, (0, 0))
        title = gamefont.render("Settings", True, WHITE)
        title_rect = title.get_rect(center=(WIDTH/2, 50))
        SCREEN.blit(title, title_rect)

        if DIFLEVEL == 0:
            off = gamefont.render("Off", True, (255, 0, 0))
            off_rect = off.get_rect(midleft=(900, HEIGHT / 2 - 50))
            SCREEN.blit(off, off_rect)
        else:
            on = gamefont.render("On", True, (0, 255, 0))
            on_rect = on.get_rect(midleft=(900, HEIGHT / 2 - 50))
            SCREEN.blit(on, on_rect)

        if SEF.Check_Sound():
            on = gamefont.render("On", True, (0, 255, 0))
            on_rect = on.get_rect(midleft=(900, HEIGHT / 2))
            SCREEN.blit(on, on_rect)
        else:
            off = gamefont.render("Off", True, (255, 0, 0))
            off_rect = off.get_rect(midleft=(900, HEIGHT / 2))
            SCREEN.blit(off, off_rect)
            
        if SOUND_STATUS == 1:
            on = gamefont.render("On", True, (0, 255, 0))
            on_rect = on.get_rect(midleft=(900, HEIGHT / 2 + 50))
            SCREEN.blit(on, on_rect)
        else:
            off = gamefont.render("Off", True, (255, 0, 0))
            off_rect = off.get_rect(midleft=(900, HEIGHT / 2 + 50))
            SCREEN.blit(off, off_rect)
            
        for i, item in enumerate(setsubmenu_items):
            if item == "Return":
                sitems = gamefont.render(item, True, WHITE if i == selected_item else (100, 100, 100))
                sitems_rect = sitems.get_rect(center=(WIDTH / 2, HEIGHT - 50))
            else:
                sitems = gamefont.render(item, True, WHITE if i == selected_item else (100, 100, 100))
                sitems_rect = sitems.get_rect(midleft=(300, HEIGHT / 2 - 50 + i * 50))
            SCREEN.blit(sitems, sitems_rect)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected_item > 0:
                        selected_item -= 1
                elif event.key == pygame.K_DOWN:
                    if selected_item < len(setsubmenu_items) - 1:
                        selected_item += 1
                elif event.key == pygame.K_RETURN:
                    return selected_item


# -Δημιουργία Παίχτη
def player():
    p_top_left = 0
    p_height = 100
    p_width = 25  
    tplayer = pygame.Rect(0, 0,p_width,p_height)
    return tplayer

# -Δημιουργία Μπάλας
class ball():
    def tball():
        b_size = 50    
        ball = pygame.Rect(0, 0, b_size, b_size)
        return ball

# -Θέση Αριστερου Παιχτη
def lplayer():
    tplayer = player()
    tplayer.x = 100
    tplayer.y = HEIGHT/2 - tplayer.y/2
    return tplayer
    
# -Θέση Δεξιου Παιχτη
def rplayer():
    tplayer = player()
    tplayer.x = WIDTH - tplayer.width - 100 
    tplayer.y = HEIGHT/2 - tplayer.y/2
    return tplayer

# - Ταχύτητα Παικτών
def splayers():
    player1 = 0.25
    player2 = 0.25
    tplayer = [player1,player2]
    return tplayer

# -Αρχική Θέση Μπάλας
def cball():
    tball = ball.tball()
    tball.x = WIDTH/2 - tball.width/2
    tball.y = HEIGHT/2 - tball.width/2
    return tball

# -Παράμετροι Ταχύτητας Μπάλας
def speedlimits():     
    upper_limit_x = 0.3
    lower_limit_x = 0.15
    upper_limit_y = 0.3
    lower_limit_y = 0
    tspeed = [upper_limit_x,lower_limit_x,upper_limit_y,lower_limit_y]
    return tspeed

# -Ταχύτητα Αρχικής Μπάλας
def ballspeed():
    tspeed = speedlimits()
    if random.randint(0,1) == 0: #H Μπαλα θα πάει δεξιά ή αριστερα 
        tspeed[0] = -1 * tspeed[0] 
    if random.randint(0,1) == 0: #Η μπάλα θα πάει πάνω ή κάτω 
        tspeed[1] = -1 * tspeed[1] 
    tspeed[0] = tspeed[0] * random.uniform (0.8,1.3)
    tspeed[1] = tspeed[1] * random.uniform (0.8,1.3)    
    return tspeed


# - Μεταβολή Ταχύτητας Μπάλας
def fspeed(speed_x, speed_y):
    lspeed = speedlimits()
    tspeed = [speed_x, speed_y]
    
    xfactor = random.uniform(lspeed[0],lspeed[1])
    if  speed_x < 0:
        tspeed[0] = -xfactor
    else:
        tspeed[0] = xfactor

    xfactor = random.uniform(lspeed[2],lspeed[3])
    if speed_y < 0 :
        tspeed[1] = -xfactor
    else:
        tspeed[1] = xfactor

    return tspeed


# -ScoreBoard
def scoreboard(shome,saway):
    text = gamefont.render(shome, True, BLACK )
    text_rect = text.get_rect(center=(WIDTH/2 - 100, 100 ))
    SCREEN.blit(text, text_rect)
    text = gamefont.render(saway, True, BLACK )
    text_rect = text.get_rect(center=(WIDTH/2 + 100, 100 ))
    SCREEN.blit(text, text_rect)

def GamePlayMask():
    pygame.draw.rect(SCREEN,RED,[0, 0, WIDTH, HEIGHT],10)
    pygame.draw.rect(SCREEN,RED,pygame.Rect(490, 10, 300, 120),  10, 3)
    pygame.draw.rect(SCREEN,BLACK,pygame.Rect(640, 150, 10, 550), 0, 3)


# -Αντίστροφη μέτρηση
def rcounter(tvalue,ntime,emode):    
    rvalue = [tvalue,ntime,emode]
    rtime = pygame.time.get_ticks()    
    if rtime - rvalue[1] > 0:        
        if rvalue[0] != "0":
            rvalue[0] = str(int(rvalue[0]) - 1)            
            rvalue[1] = rtime + 1000
            rvalue[2] = 0
        else:
            rvalue[0] = RTIMER
            rvalue[2] = 1          
    text = gamefont.render(rvalue[0], True, BLACK )
    text_rect = text.get_rect(center=(WIDTH/2 , 50))
    SCREEN.blit(text, text_rect)    
    return rvalue

# -GameStatus
def gamestatus(shome,saway) :
    if shome == "10" :
        text = gamefont.render(" HOME TEAM WINS ", True, (250,0,0) )
        text_rect = text.get_rect(center=(WIDTH/2 , HEIGHT/2))
        SCREEN.blit(text, text_rect)
        PlayWin_SF()        
        return True
    elif saway == "10" :
        text = gamefont.render(" GUEST TEAM WINS ", True, (0,250,0) )
        text_rect  = text.get_rect(center=(WIDTH/2 , HEIGHT/2))
        SCREEN.blit(text, text_rect )  
        PlayWin_SF()    
        return True
    else :
        return False

# -Παίζει ο ήχος όταν χτυπήσει η μπάλα στην ρακέτα
def PlayImpact_SF():
    if SOUND_STATUS == 1:
        SEF.Impact_Sound.play(1)

# -Πάζει ο ήχος όταν σκοράρει κάποιος
def PlayPoint_SF():
    if SOUND_STATUS == 1:
        SEF.Point_Sound.play(1)

def PlayWin_SF():
    if SOUND_STATUS == 1:
        SEF.Win_Sound.set_volume(0.6)
        SEF.Win_Sound.play(1)

# -Function για να παίξεις εναντίον άλλου παικτή-
 
def play_vs_player():
    
#Δημιοργία Παικτών    
    rect_1 = lplayer()
    rect_2 = rplayer()    

    #Λίστες για τις μπάλες μας και τις ταχύτητες τους
    rballs = []
    sballs = []    

    #Απόσταση πάικτη απο τα άκρα 
    padding = 5

    #Εισαγωγή τιμών ταχύτητας παικτη
    splayer = splayers()        
    
    shome = "0"
    saway = "0"

    # Χρόνος παιχνιδιου
    clock = pygame.time.Clock()

    # Χρόνος αντίστροφής μέτρησης, χρόνος + 1sec
    rvalue = [RTIMER, pygame.time.get_ticks()+1000,0]   
    
    running = True

    #Παραμετρος για την καθυστερηση κατα ενα κύκλο επι συντελεστή της ανιχνευσης σύγκρουσης για την αποφυγη εσωτερικών αναπηδήσεων
    delayC = 500
    #Βοηθητική τιμή για την καθυστέρηση σύγκρουσης
    ttemp = []

    tt1 = 0
    tt2 = 0
    
    while running:              
        # περιορισμός FPS σε 60
        # dt είναι η διαφορά χρόνου απο το τελευταιο frame        
        dt = clock.tick(FPS)
        
        # έλεγχος για events
        # pygame.QUIT event όταν ο χρήστης πατήσει το X κλεινει το παράθυρο
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Γεμιζουμε την οθόνη μας με το χρώμα επιλογής μας 
        #SCREEN.fill("black") 
        SCREEN.blit(GamePlayIMG, (0, 0))
        GamePlayMask()
        #pygame.display.update()

        #Δημιουργουμε τα γεωμετρικά σχήματα των παικτων
        pygame.draw.rect(SCREEN, "black", rect_1)
        pygame.draw.rect(SCREEN, "black", rect_2)     
       
        #Δημιουργία  Αρχικής Μπάλας
        if len(rballs) == 0:
            rballs = [cball()]
            sballs = [ballspeed()]
            ttemp = [0]
            pygame.draw.rect(SCREEN, "black", rballs[0] )
            
        # Αν έχουμε βαθμό δυσκολίας ενεργοποιούμε το χρονόμετρο
        if (DIFLEVEL > 0 ):
            rvalue = rcounter(rvalue[0], rvalue[1], rvalue[2])
            #Όταν το χρονόμετρο μηδενίσει δημιουργει έξτρα μπάλες
            if rvalue[2] == 1:
                if len(rballs) >= 1 :
                    for i in range(len(rballs),len(rballs) + 3):
                        rballs.append(cball())
                        sballs.append(ballspeed())
                        ttemp.append(0)

        # Μετακινούμε όλες τις μπάλες που υπάρχουν στο παιχνίδι        
        for i in range (0,len(rballs)) :
                pygame.draw.rect(SCREEN, "black", rballs[i] )
                rballs[i].x += sballs[i][0] * dt
                rballs[i].y += sballs[i][1] * dt
                   

        # Ταμπλο για αλλαγη σκορ
        scoreboard(shome,saway)             


        #Αν πατήσουμε κάποιο κουμπί
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and rect_1.y > 5:
            rect_1.y -= splayer[0] * dt
            
        if keys[pygame.K_s] and rect_1.y < HEIGHT - rect_1.height -5 :
            rect_1.y += splayer[0] * dt       
       
        if keys[pygame.K_UP] and rect_2.y > 5:
            rect_2.y -= splayer[1] * dt
            
        if keys[pygame.K_DOWN] and rect_2.y < HEIGHT - rect_2.height -5 :
            rect_2.y += splayer[1] * dt

       
#Αναπήδηση της μπαλας όταν χτυπήσει πάνω ή κάτω              
        for i in range (0,len(rballs)) :
            if (rballs[i].y < 1 or rballs[i].y > HEIGHT - rballs[i].width - 1):
                if rballs[i].y < 1:
                    rballs[i].y = 1
                if rballs[i].y > HEIGHT - rballs[i].width - 1:
                    rballs[i].y = HEIGHT - rballs[i].width - 1
                if DIFLEVEL > 0: #Extra δυσκολια 
                    sballs[i] = fspeed(sballs[i][0],sballs[i][1])
                sballs[i][1] = -1 *  sballs[i][1] 
                PlayImpact_SF() #Αν η μπαλα προσκρουσει στην ρακετα ενεργοποιείται ο ηχος

        

        #Αν η μπαλα χτυπήσει αριστερά ή δεξιά 
        t = [] #Βοηθητική μεταβλητή γιατί οταν η μπαλα κτυπαει αριστερα ή δεξιά καταστρέφεται
        for i in range (0,len(rballs)) :            
            if (rballs[i].x < 1 or rballs[i].x > WIDTH - rballs[i].width - 1):    
                if rballs[i].x < 1:               
                    if gameover == False:
                        saway = str(int(saway) + 1)   #Μπήκε γκολ αριστερα                 
                if rballs[i].x > WIDTH - rballs[i].width - 1:                
                    if gameover == False:
                        shome = str(int(shome) + 1) #Μπήκε γκόλ δεξια
                t.append(i) #Αποθηκεύουμε τον δείκτη της μπάλας που μπήκε γκόλ δεν σβήνουμε απευθείας γιατί βγαίνουμε εκτός ορίων λίστας
        if len(t)>0:
            t.sort(reverse = True) 
            for i in t: #σβήνουμε στοχευμένα
                rballs.remove(rballs[i])
                sballs.remove(sballs[i])
                ttemp.remove(ttemp[i])
                PlayPoint_SF()#Αν η μπαλα μπει γκολ
        gameover = gamestatus(shome,saway)

        if gameover == True :
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:               
                running = False           
                   
                    
        #Αναπήδηση της μπαλας όταν χτυπήσει την αριστερή μπάρα        
        for i in range (0,len(rballs)) :
            if rect_1.colliderect(rballs[i]) and ttemp[i] <= 0 :
                sballs[i] = fspeed(sballs[i][0],sballs[i][1])        
                ttemp[i] = delayC
                rballs[i].x = rballs[i].x - sballs[i][0]
                rballs[i].y = rballs[i].y - sballs[i][1]            
                sballs[i][0] = -1 *  sballs[i][0]
                PlayImpact_SF() #Αν η μπαλα προσκρουσει στην ρακετα ενεργοποιείται ο ηχος
            else :
                # Χρονοκαθυστέρηση για την αποφυγη εσωτερικών αναπηδησεων
                ttemp[i] = ttemp[i] - dt
                

        #Αναπήδηση της μπαλας όταν χτυπήσει την δεξιά μπάρα     
        for i in range (0,len(rballs)) :
            if rect_2.colliderect(rballs[i]) and ttemp[i] <= 0 :
                sballs[i] = fspeed(sballs[i][0],sballs[i][1])        
                ttemp[i] = delayC
                rballs[i].x = rballs[i].x - sballs[i][0]
                rballs[i].y = rballs[i].y - sballs[i][1]            
                sballs[i][0] = -1 * sballs[i][0]
                PlayImpact_SF() #Αν η μπαλα προσκρουσει στην ρακετα ενεργοποιείται ο ηχος
            else :
                # Χρονοκαθυστέρηση για την αποφυγη εσωτερικών αναπηδησεων
                ttemp[i] = ttemp[i] - dt     
        
        
        # flip() την οθόνη για να δείξουμε τα γραφικά μας 
        pygame.display.flip()
      

        if len(sballs)>0:
            if (tt1 != sballs[0][0] or tt2 !=sballs[0][1]):
                    tt1 = sballs[0][0]
                    tt2 = sballs[0][1]
                    print ("speed x : ", tt1, "speed y : ", tt2)    


        
# -Function για να παίξεις εναντίον του υπολογιστή- 
def play_vs_computer():

    #Δημιοργία Παικτών    
    rect_1 = lplayer()
    rect_2 = rplayer()    

    #Λίστες για τις μπάλες μας και τις ταχύτητες τους
    rballs = []
    sballs = []    

    #Απόσταση πάικτη απο τα άκρα 
    padding = 5

    #Εισαγωγή τιμών ταχύτητας παικτη
    splayer = splayers()        
    
    shome = "0"
    saway = "0"

    # Χρόνος παιχνιδιου
    clock = pygame.time.Clock()

    # Χρόνος αντίστροφής μέτρησης, χρόνος + 1sec
    rvalue = [RTIMER, pygame.time.get_ticks()+1000,0]   
    
    running = True

    #Παραμετρος για την καθυστερηση κατα ενα κύκλο επι συντελεστή της ανιχνευσης σύγκρουσης για την αποφυγη εσωτερικών αναπηδήσεων
    delayC = 500
    #Βοηθητική τιμή για την καθυστέρηση σύγκρουσης
    ttemp = []

    tt1 = 0
    tt2 = 0

    gameover = False
    
    while running:              
        # περιορισμός FPS σε 60
        # dt είναι η διαφορά χρόνου απο το τελευταιο frame        
        dt = clock.tick(FPS)
        
        # έλεγχος για events
        # pygame.QUIT event όταν ο χρήστης πατήσει το X κλεινει το παράθυρο
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Γεμιζουμε την οθόνη μας με το χρώμα επιλογής μας 
        #SCREEN.fill("black") 
        SCREEN.blit(GamePlayIMG, (0, 0))
        GamePlayMask()
        #pygame.display.update()

        #Δημιουργουμε τα γεωμετρικά σχήματα των παικτων
        pygame.draw.rect(SCREEN, "black", rect_1)
        pygame.draw.rect(SCREEN, "black", rect_2)     


        if gameover == False :        
            #Δημιουργία  Αρχικής Μπάλας
            if len(rballs) == 0:
                rballs = [cball()]
                sballs = [ballspeed()]
                ttemp = [0]
                pygame.draw.rect(SCREEN, "black", rballs[0] )
            
            # Αν έχουμε βαθμό δυσκολίας ενεργοποιούμε το χρονόμετρο
            if (DIFLEVEL > 0 ):
                rvalue = rcounter(rvalue[0], rvalue[1], rvalue[2])
                #Όταν το χρονόμετρο μηδενίσει δημιουργει έξτρα μπάλες
                if rvalue[2] == 1:
                    if len(rballs) >= 1 :
                        for i in range(len(rballs),len(rballs) + 3):
                            rballs.append(cball())
                            sballs.append(ballspeed())
                            ttemp.append(0)

            # Μετακινούμε όλες τις μπάλες που υπάρχουν στο παιχνίδι        
            for i in range (0,len(rballs)) :
                    pygame.draw.rect(SCREEN, "black", rballs[i] )
                    rballs[i].x += sballs[i][0] * dt
                    rballs[i].y += sballs[i][1] * dt
                   

        # Ταμπλο για αλλαγη σκορ
        scoreboard(shome,saway)             

        
        #Αν πατήσουμε κάποιο κουμπί
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and rect_1.y > 5:
            rect_1.y -= splayer[0] * dt            
        if keys[pygame.K_s] and rect_1.y < HEIGHT - rect_1.height -5 :
            rect_1.y += splayer[0] * dt  


        # Κίνηση απο υπολογιστη
        mindistance = 0
        mintemp = 0
        if len(rballs)>0 :
            for i in range (0,len(rballs)) :
                if i == 0 :
                    mindistance = (WIDTH-rballs[i].x)^2+(rect_2.y-rballs[i].y)^2
                    mintemp = i
                else :
                    if mindistance < (WIDTH-rballs[i].x)^2+(rect_2.y-rballs[i].y)^2:
                        mintemp = i 
            if (rect_2.y + rect_2.height/2) - (rballs[mintemp].y + rballs[mintemp].width/2) > 0 and rect_2.y > 0 and (rect_2.y + rect_2.height) < HEIGHT :   
                rect_2.y -= splayer[1] * dt
            if (rect_2.y + rect_2.height/2) - (rballs[mintemp].y + rballs[mintemp].width/2) < 0 and rect_2.y > 0 and (rect_2.y + rect_2.height) < HEIGHT :
                rect_2.y += splayer[1] * dt
            if rect_2.y <  padding :
                rect_2.y =  padding
            if ( HEIGHT - (rect_2.y + rect_2.height) <  padding ):
                rect_2.y = HEIGHT - rect_2.height -  padding
            
       
        #Αναπήδηση της μπαλας όταν χτυπήσει πάνω ή κάτω              
        for i in range (0,len(rballs)) :
            if (rballs[i].y < 1 or rballs[i].y > HEIGHT - rballs[i].width - 1):
                if rballs[i].y < 1:
                    rballs[i].y = 1
                if rballs[i].y > HEIGHT - rballs[i].width - 1:
                    rballs[i].y = HEIGHT - rballs[i].width - 1
                if DIFLEVEL > 0: #Extra δυσκολια 
                    sballs[i] = fspeed(sballs[i][0],sballs[i][1])
                sballs[i][1] = -1 *  sballs[i][1] 
                PlayImpact_SF() #Αν η μπαλα προσκρουσει στην ρακετα ενεργοποιείται ο ηχος

        

        #Αν η μπαλα χτυπήσει αριστερά ή δεξιά 
        t = [] #Βοηθητική μεταβλητή γιατί οταν η μπαλα κτυπαει αριστερα ή δεξιά καταστρέφεται
        for i in range (0,len(rballs)) :            
            if (rballs[i].x < 1 or rballs[i].x > WIDTH - rballs[i].width - 1):    
                if rballs[i].x < 1:               
                    if gameover == False:
                        saway = str(int(saway) + 1)   #Μπήκε γκολ αριστερα                 
                if rballs[i].x > WIDTH - rballs[i].width - 1:                
                    if gameover == False:
                        shome = str(int(shome) + 1) #Μπήκε γκόλ δεξια
                t.append(i) #Αποθηκεύουμε τον δείκτη της μπάλας που μπήκε γκόλ δεν σβήνουμε απευθείας γιατί βγαίνουμε εκτός ορίων λίστας
        if len(t)>0:
            t.sort(reverse = True) 
            for i in t: #σβήνουμε στοχευμένα
                rballs.remove(rballs[i])
                sballs.remove(sballs[i])
                ttemp.remove(ttemp[i])
                PlayPoint_SF()#Αν η μπαλα μπει γκολ
        gameover = gamestatus(shome,saway)

        if gameover == True :
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:               
                running = False           
                   
                    
        #Αναπήδηση της μπαλας όταν χτυπήσει την αριστερή μπάρα        
        for i in range (0,len(rballs)) :
            if rect_1.colliderect(rballs[i]) and ttemp[i] <= 0 :
                sballs[i] = fspeed(sballs[i][0],sballs[i][1])        
                ttemp[i] = delayC
                rballs[i].x = rballs[i].x - sballs[i][0]
                rballs[i].y = rballs[i].y - sballs[i][1]            
                sballs[i][0] = -1 *  sballs[i][0]
                PlayImpact_SF() #Αν η μπαλα προσκρουσει στην ρακετα ενεργοποιείται ο ηχος
            else :
                # Χρονοκαθυστέρηση για την αποφυγη εσωτερικών αναπηδησεων
                ttemp[i] = ttemp[i] - dt
                

        #Αναπήδηση της μπαλας όταν χτυπήσει την δεξιά μπάρα     
        for i in range (0,len(rballs)) :
            if rect_2.colliderect(rballs[i]) and ttemp[i] <= 0 :
                sballs[i] = fspeed(sballs[i][0],sballs[i][1])        
                ttemp[i] = delayC
                rballs[i].x = rballs[i].x - sballs[i][0]
                rballs[i].y = rballs[i].y - sballs[i][1]            
                sballs[i][0] = -1 * sballs[i][0]
                PlayImpact_SF() #Αν η μπαλα προσκρουσει στην ρακετα ενεργοποιείται ο ηχος
            else :
                # Χρονοκαθυστέρηση για την αποφυγη εσωτερικών αναπηδησεων
                ttemp[i] = ttemp[i] - dt     
        
        
        # flip() την οθόνη για να δείξουμε τα γραφικά μας 
        pygame.display.flip()
      

        if len(sballs)>0:
            if (tt1 != sballs[0][0] or tt2 !=sballs[0][1]):
                    tt1 = sballs[0][0]
                    tt2 = sballs[0][1]
                    print ("speed x : ", tt1, "speed y : ", tt2)

# --Μενού Ελέγχου--
 
while True:
    choiceM = main_menu() #Εδώ καλείται το Function του κεντρικού μενού και παρακάτω γίνεται ο ελεγχός των στοιχείων του
    if choiceM == 0: # Play
        while True:
            choiceP = playsubmenu() #Εδώ καλείται το Function του υπομενού Play και παρακάτω γίνεται ο ελεγχός των στοιχείων του
            if choiceP == 0: # Versus Player
                play_vs_player()
            elif choiceP == 1: # Versus Computer
                play_vs_computer()
            elif choiceP == 2: # Return
                break # Επιστροφή στο αρχικό μενού
    elif choiceM == 1: # Settings
        while True:
            choiceS = setsubmenu() #Εδώ καλείται το Function του υπομενού Settings και παρακάτω γίνεται ο ελεγχός των στοιχείων του και γινονται οι αλλαγές στις μεταβλήτες ανάλογα με τις προτιμήσεις μας
            if choiceS == 0: # Hard Mode
                if DIFLEVEL == 0:
                    DIFLEVEL = 1
                else:
                    DIFLEVEL = 0
            elif choiceS == 1: # Music
                if SEF.Check_Sound():
                    SEF.Backround_Sound.stop()
                else:
                    SEF.Backround_Sound.play()
            elif choiceS == 2: # Sound Effects
                if SOUND_STATUS == 1:
                    SOUND_STATUS = 0
                else:
                    SOUND_STATUS = 1
            elif choiceS == 3: # Return
                break # Επιστροφή στο αρχικό μενού
    elif choiceM == 2: # Quit
        pygame.quit()
        sys.exit()
