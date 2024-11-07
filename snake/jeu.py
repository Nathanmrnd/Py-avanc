import pygame
import argparse


MIN_SIZE = 200
W_DEFAULT =  500
H_DEFAULT = 500


def argue():

    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('-L', type=int, help="Width")
    parser.add_argument('-l', type=int, help="Heights")
    args = parser.parse_args()

    

    # Check argument
    if min(args.L,args.l) < MIN_SIZE:
        raise ValueError("The size (-s argument) must be greater or equal to %d." % MIN_SIZE)
    
    return args

def echiquier(screen,w,h,n): #n**2:nombre de case 
    screen.fill( (0, 255, 0) )
    black = (0, 0, 0)   
    white = (255,255,255)
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





def game():
    args=argue()
    (w,h)=(args.L,args.l)
    n=16 #nombre de ligne/colonne
    #o initialise la localisation du snake
    localisation=[(w/5 + (n//2 - 2)*w*3/(5*n), h/5+ (n//2)*h*3/(5*n)),(w/5 + (n//2 -1)*w*3/(5*n), h/5+ (n//2)*h*3/(5*n)),(w/5 + (n//2)*w*3/(5*n), h/5+ (n//2)*h*3/(5*n))]
    pygame.init() 
    screen = pygame.display.set_mode( (w, h) )
    pygame.display.set_caption("Snape")
    

    clock = pygame.time.Clock()


    while True:
        # Wait one second, starting from last display or now
        clock.tick(1)
        echiquier(screen,w,h,n)
        snake(screen, localisation,n,w,h)
        # Process new events (keyboard, mouse)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.key == pygame.K_q:
                    return True



    pygame.quit()
    return args





def screen():
    (w,h)=(W_DEFAULT,H_DEFAULT)
    pygame.init()   
    screen = pygame.display.set_mode( (w, h) )



    clock = pygame.time.Clock()
    while True:
        # Wait one second, starting from last display or now
        clock.tick(1)
        # Process new events (keyboard, mouse)
        for event in pygame.event.get():
            pass # do nothing for the moment
        screen.fill( (0, 255, 0) ) # Fill screen with green
        color = (0, 0, 255) # blue
        rect = pygame.Rect(w/5, h/5, w*3/5, h*3/5)
        pygame.draw.rect(screen, color, rect)
        pygame.display.update()

    pygame.quit()

