import pygame
import argparse


MIN_SIZE = 200
W_DEFAULT =  500
H_DEFAULT = 500
nathan =0

def argue():

    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('-L', type=int, help="Width")
    parser.add_argument('-l', type=int, help="Heights")
    args = parser.parse_args()
    return args

    # Check argument
    #if args.s < MIN_SIZE:
     #   raise ValueError("The size (-s argument) must be greater or equal to %d." % MIN_SIZE)

def echiquier(w,h,n): #n**2:nombre de case 
    screen = pygame.display.set_mode( (w, h) )
    pygame.display.set_caption("Snape")
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


def snake(t,locx,locy,n,w,h):
    green=(0,255,0)
    rect=pygame.Rect(locx,locy,w*3/(5*n), h*3/(5*n))





def screen():
    (w,h)=(W_DEFAULT,H_DEFAULT)
    pygame.init() 
    n=15
    echiquier(w,h,n)

    clock = pygame.time.Clock()


    while True:
        # Wait one second, starting from last display or now
        clock.tick(1)
        # Process new events (keyboard, mouse)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return True



    pygame.quit()