import pygame
import argparse
import random as rd
import math

MIN_SIZE = 200
W_DEFAULT =  500
H_DEFAULT = 500

class Serpent:
    def __init__(self,localisation,tete):
        self.localistion = localisation
        self.tete = tete
    def __repr__(self):
        return (localisation,tete)


class Case:
    def __init__(self,i,j,color,w,h,n,screen): 
        self.locx = w/5 + (i)*w*3/(5*n)
        self.locy = h/5+ (j)*h*3/(5*n)
        self.aretx = w*3/(5*n)
        self.arety = h*3/(5*n)
        self.color = color
        self.screen = screen

    def __repr__(self):
        return f"Cases de coordonnées {self.locx},{self.locy}"

    def dessin(self):
        rect = pygame.Rect(self.locx, self.locy, self.aretx, self.arety)
        pygame.draw.rect(self.screen, self.color, rect)
        pygame.display.update()




class Echiquierclass:
    def __init__(self,w,h,n,screen):
        self.screen = screen
        self.w = w
        self.h = h
        self.n = n

    def __repr__(self):
        return f"Hello"
    
    def draw(self):
        black = (0, 0, 0)   
        white = (255,255,255)
        self.screen.fill(black)
    
        for i in range(self.n):
            for j in range(self.n):
                if (i+j)%2==0 :
                    color=white
                else:                    
                    color=black
                caseij= Case(i,j,color,self.w,self.h,self.n,self.screen)
                caseij.dessin()
                





def argue(): #permet à l'utilsateur de choisir la hauteur (heights) et la largeur (width) de la fenetre de jeu

    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('-L', type=int, help="Width", default=W_DEFAULT)
    parser.add_argument('-l', type=int, help="Heights", default=H_DEFAULT)
    args = parser.parse_args()

    

    # Check argument
    if min(args.L,args.l) < MIN_SIZE:
        raise ValueError("The size (-s argument) must be greater or equal to %d." % MIN_SIZE)
    
    return args




def snake(screen,Localisation,n,w,h): #localisation : liste contenant les coordonées de chaque rectangle du snake
    green=(0,255,0)
    for (locx,locy) in Localisation:
        case1=Case(locx,locy,green,w,h,n,screen)
        case1.dessin()
        

def fruit(eaten,n,w,h,screen,coordfruit): #eaten est un booléen indiquant si le fruit a été mangé ou pas
    red = (255,0,0)
    
    if eaten: 
        i = rd.randint(0,n-1)
        j= rd.randint(0,n-1)
        coordfruit=(i,j)
        casefruit = Case(i,j,red,w,h,n,screen)
        casefruit.dessin()
        eaten = False
    else :
        (i,j)=coordfruit
        casefruit = Case(i,j,red,w,h,n,screen)
        casefruit.dessin()
    return (coordfruit,eaten)


def eatthefruit(eaten,n,w,h,screen,localisation,coordfruit):
    if localisation[-1]==coordfruit :
        localisation.insert(0, localisation[0])
        eaten=True
    return (localisation,eaten)


def déplacement_droite(localisation,w,h,n,screen):
    black = (0, 0, 0)   
    white = (255,255,255)
    if (localisation[0][0]+localisation[0][1])%2==0 :
        color = white
    else:                    
        color = black
    case0=Case(localisation[0][0],localisation[0][1],color,w,h,n,screen) #case qu'il faut redessiner
    case0.dessin()
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx+1,locy)
    localisation.append((locx,locy))
    return localisation

def déplacement_bas(localisation,w,h,n,screen):
    black = (0, 0, 0)   
    white = (255,255,255)
    if (localisation[0][0]+localisation[0][1])%2==0 :
        color = white
    else:                    
        color = black
    case0=Case(localisation[0][0],localisation[0][1],color,w,h,n,screen) #case qu'il faut redessiner
    case0.dessin()
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx,locy+1)
    localisation.append((locx,locy))
    return localisation

def déplacement_haut(localisation,w,h,n,screen):
    black = (0, 0, 0)   
    white = (255,255,255)
    if (localisation[0][0]+localisation[0][1])%2==0 :
        color = white
    else:                    
        color = black
    case0=Case(localisation[0][0],localisation[0][1],color,w,h,n,screen) #case qu'il faut redessiner
    case0.dessin()
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx,locy-1)
    localisation.append((locx,locy))
    return localisation

def déplacement_gauche(localisation,w,h,n,screen):
    black = (0, 0, 0)   
    white = (255,255,255)
    if (localisation[0][0]+localisation[0][1])%2==0 :
        color = white
    else:                    
        color = black
    case0=Case(localisation[0][0],localisation[0][1],color,w,h,n,screen) #case qu'il faut redessiner
    case0.dessin()
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx-1,locy)
    localisation.append((locx,locy))
    return localisation


def doublon(localisation):
    
    for i in range(len(localisation)):
        for j in range(i + 1, len(localisation)):
            if localisation[i] == localisation[j]:
                return True
    return False

def perdu(localisation,n,w,h,screen):
    tete = localisation[-1]  
    nx, ny = tete
    if nx < 0 or nx >= n or ny < 0 or ny >= n or localisation.count(tete) > 1:
        font = pygame.font.SysFont(None, 55)
        text = font.render("LOOOOSER", True, (255, 0, 0))
        screen.fill((0, 0, 0))
        screen.blit(text, ((w - text.get_width()) // 2, (h - text.get_height()) // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit() 
        quit() 


def score(screen, localisation, w, h,n):
    font = pygame.font.SysFont(None, 35)
    longueur = len(localisation)
    text = font.render(f"Score : {longueur}", True, (255, 255, 255)) 
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, w, 50)) #on efface le score précédent 
    screen.blit(text, (10, 10)) 
    pygame.display.update()



def game():
    args=argue()
    (w,h)=(args.L,args.l)
    eaten = True
    coordfruit=(0,0)
    n=15 #nombre de ligne/colonne
    #on initialise la localisation du snake
    localisation=[(n//2,n//4),(n//2,n//4 +1),(n//2,n//4 +2)]
    direction = 'Droite'
    pygame.init() 
    screen = pygame.display.set_mode( (w, h) )
    echi = Echiquierclass(W_DEFAULT,H_DEFAULT,15,pygame.display.set_mode( (W_DEFAULT, H_DEFAULT) ))
    echi.draw()   
    pygame.display.set_caption("Snape")
    

    clock = pygame.time.Clock()
    i=0

    while True:
        i+=1
        # Wait one second, starting from last display or now
        clock.tick(1+i/20) #à adapter en fonction des envies
        (localisation,eaten)=eatthefruit(eaten,n,w,h,screen,localisation,coordfruit)
        (coordfruit,eaten)=fruit(eaten,n,w,h,screen,coordfruit)
        # Process new events (keyboard, mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                return True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    return True
                if event.key == pygame.K_DOWN :
                    direction = 'Bas'
                if event.key == pygame.K_LEFT :
                    direction = 'Gauche'
                if event.key == pygame.K_UP :
                    direction = 'Haut'
                if event.key == pygame.K_RIGHT :
                    direction = 'Droite'
        

        if direction == 'Haut':
            localisation = déplacement_haut(localisation,w,h,n,screen)
        if direction == 'Bas':
            localisation = déplacement_bas(localisation,w,h,n,screen)
        if direction == 'Droite':
            localisation = déplacement_droite(localisation,w,h,n,screen)
        if direction == 'Gauche':
            localisation = déplacement_gauche(localisation,w,h,n,screen)
            
        score(screen,localisation,w,h,n)
        perdu(localisation,n,w,h,screen)
         
        snake(screen, localisation,n,w,h) #on redessine le serpent à sa nouvelle position à chaque fois
        pygame.display.update() 
        

    pygame.quit()
    


