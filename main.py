import pygame

pygame.init()

WIDTH = 500
HEIGHT = 450
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess Game")
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60

# Important Game Variables
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),] # (x, y)

black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),] # (x, y)

captured_pieces_white = []
captured_pieces_black = []
turn_step = 0 # 0 is white's turn , 1 is white's turn and piece has been selected, 
              # 2 is black's turn and 3 is black's turn with a piece selected or moved
selection = 100
valid_moves = []
# load in game images
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (40, 40))
black_queen_small = pygame.transform.scale(black_queen, (20, 20))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (40, 40))
black_king_small = pygame.transform.scale(black_king, (20, 20))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (40, 40))
black_rook_small = pygame.transform.scale(black_rook, (20, 20))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (40, 40))
black_bishop_small = pygame.transform.scale(black_bishop, (20, 20))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (40, 40))
black_knight_small = pygame.transform.scale(black_knight, (20, 20))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (20, 20))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (40, 40))
white_queen_small = pygame.transform.scale(white_queen, (20, 20))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (40, 40))
white_king_small = pygame.transform.scale(white_king, (20, 20))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (40, 40))
white_rook_small = pygame.transform.scale(white_rook, (20, 20))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (40, 40))
white_bishop_small = pygame.transform.scale(white_bishop, (20, 20))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (40, 40))
white_knight_small = pygame.transform.scale(white_knight, (20, 20))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (20, 20))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]

piece_list = ['pawn','rook', 'knight', 'bishop', 'queen', 'king']

def draw_Board():
    for i in range(32):
        column = i % 4 # remainder 4
        row = i // 4 # rounds down to the nearest whole integer
        if row % 2 == 0:
            pygame.draw.rect(screen, "light grey", [300 - (column * 100), row * 50, 50, 50])
        else:
            pygame.draw.rect(screen, "light grey", [350 - (column * 100), row * 50, 50, 50])
        pygame.draw.rect(screen, 'gray', [0, 400, WIDTH, 50])
        pygame.draw.rect(screen, 'gold', [0, 400, WIDTH, 50], 3)
        pygame.draw.rect(screen, 'gold', [400, 0, 100, HEIGHT], 3)

# Game While Loop
run = True
while run:
    timer.tick(fps)
    screen.fill("dark gray")
    draw_Board()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()

pygame.quit()