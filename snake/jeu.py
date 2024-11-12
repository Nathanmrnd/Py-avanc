import pygame
import argparse


MIN_SIZE = 200
W_DEFAULT =  500
H_DEFAULT = 500


def argue(): #permet à l'utilsateur de choisir la hauteur (heights) et la largeur (width) de la fenetre de jeu

    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('-L', type=int, help="Width", default=W_DEFAULT)
    parser.add_argument('-l', type=int, help="Heights", default=H_DEFAULT)
    args = parser.parse_args()

    

    # Check argument
    if min(args.L,args.l) < MIN_SIZE:
        raise ValueError("The size (-s argument) must be greater or equal to %d." % MIN_SIZE)
    
    return args

def echiquier(screen,w,h,n): #n**2:nombre de case 
    black = (0, 0, 0)   
    white = (255,255,255)
    screen.fill(black)
    
    for i in range(n):
        for j in range(n):
            rect = pygame.Rect(w/5 + (i)*w*3/(5*n), h/5+ (j)*h*3/(5*n), w*3/(5*n), h*3/(5*n))
            if (i+j)%2==0 :
                color=white
            else:                    
                color=black
            pygame.draw.rect(screen, color, rect)
            pygame.display.update()




def snake(screen,Localisation,n,w,h): #localisation : liste contenant les coordonées du coin haut gauche chaque rectangle du snake
    green=(0,255,0)
    for (locx,locy) in Localisation:
        rect=pygame.Rect(locx,locy,w*3/(5*n), h*3/(5*n))
        pygame.draw.rect(screen, green, rect)
        pygame.display.update()


def déplacement_droite(localisation,w,h,n):
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx+w*3/(5*n),locy)
    localisation.append((locx,locy))
    return localisation

def déplacement_bas(localisation,w,h,n):
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx,locy+h*3/(5*n))
    localisation.append((locx,locy))
    return localisation

def déplacement_haut(localisation,w,h,n):
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx,locy-h*3/(5*n))
    localisation.append((locx,locy))
    return localisation

def déplacement_gauche(localisation,w,h,n):
    localisation.remove(localisation[0])
    (locx,locy)=localisation[-1]
    (locx,locy)=(locx-w*3/(5*n),locy)
    localisation.append((locx,locy))
    return localisation


def game():
    args=argue()
    (w,h)=(args.L,args.l)
    n=16 #nombre de ligne/colonne
    #on initialise la localisation du snake
    localisation=[(w/5 + (n//2 - 2)*w*3/(5*n), h/5+ (n//2)*h*3/(5*n)),(w/5 + (n//2 -1)*w*3/(5*n), h/5+ (n//2)*h*3/(5*n)),(w/5 + (n//2)*w*3/(5*n), h/5+ (n//2)*h*3/(5*n))]
    direction = 'Droite'
    pygame.init() 
    screen = pygame.display.set_mode( (w, h) )
    pygame.display.set_caption("Snape")
    

    clock = pygame.time.Clock()


    while True:
        
        # Wait one second, starting from last display or now
        clock.tick(1)
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
            localisation = déplacement_haut(localisation,w,h,n)
        if direction == 'Bas':
            localisation = déplacement_bas(localisation,w,h,n)
        if direction == 'Droite':
            localisation = déplacement_droite(localisation,w,h,n)
        if direction == 'Gauche':
            localisation = déplacement_gauche(localisation,w,h,n)
            
        echiquier(screen,w,h,n) #il faut à chaque fois redessiner l'échiquier pour voir le déplacement du serpent
        snake(screen, localisation,n,w,h) #on redessine le serpent à sa nouvelle position à chaque fois
        

    pygame.quit()
    return args







