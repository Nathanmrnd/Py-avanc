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

