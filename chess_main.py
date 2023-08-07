import pygame as p
from CHESS import chess_engine



WIDTH= HEIGHT= 512 #400 also possible
DIMENSION= 8 # dimensions of a chess board are 8x8
SQ_SIZE= HEIGHT // DIMENSION
MAX_FPS= 15 #for animations
IMAGES={}



#global dictionary, will only be called once...


def loadImages():
    pieces=["wp","wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece]= p.transform.scale(p.image.load("images/"+ piece + ".png"), (SQ_SIZE, SQ_SIZE))
     # we can access images by using "IMAGES['wp']"



'''
from here main code starts, user input and graphic updates will be here.
'''
def main():
    p.init()
    screen= p.display.set_mode((WIDTH, HEIGHT))
    clock= p.time.Clock()
    screen.fill(p.Color("white"))
    gs= chess_engine.GameState()
    print(gs.board)

main()