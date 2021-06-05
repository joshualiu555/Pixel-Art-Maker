WIDTH = 1200
HEIGHT = 800
FPS = 60

PIXEL_SIZE = 16
COLOR_BOX_SIZE = 75
MOUSE_BOX_SIZE = 20
ICON_SIZE = 90

NUM_ROWS = int(WIDTH * 2 / 3 / PIXEL_SIZE)
NUM_COLUMNS = int(HEIGHT / PIXEL_SIZE)

NUM_COLORS = 16
RED = (255, 0, 0) #a
ORANGE = (255, 128, 0) #b
YELLOW = (255, 255, 0) #c
TAN = (255, 229, 204) #d
GREEN = (0, 102, 0) #e
LIME = (0, 255, 0) #f
BLUE = (0, 0, 255) #g
CYAN = (0, 255, 255) #h
PURPLE = (128, 0, 128) #i
HOT_PINK = (255, 31, 153) #j
LIGHT_PINK = (255, 105, 180) #k
BLACK = (0, 0, 0) #l
BROWN = (111, 78, 55) #m
DARK_GRAY = (128, 128, 128) #n
LIGHT_GRAY = (224, 224, 224) #o
WHITE = (255, 255, 255) #p
# these are practically the same as DARK_GRAY and WHITE, but they are essential to make the bucket function work
DEFAULT_DARK_GRAY = (128, 128, 127) #q
DEFAULT_WHITE = (255, 255, 254) #r

# loop through this array to visit 4 neighboring cells in bucket / floodfill function
DX, DY = {1, -1, 0, 0}, {0, 0, 1, -1}

COLOR_GRID = [[RED, ORANGE, YELLOW, TAN], [GREEN, LIME, BLUE, CYAN], [PURPLE, HOT_PINK, LIGHT_PINK, BLACK],
          [BROWN, DARK_GRAY, LIGHT_GRAY, WHITE]]
COLOR_LIST = [RED, ORANGE, YELLOW, TAN, GREEN, LIME, BLUE, CYAN, PURPLE, HOT_PINK, LIGHT_PINK, BLACK, BROWN, DARK_GRAY,
          LIGHT_GRAY, WHITE, DEFAULT_DARK_GRAY, DEFAULT_WHITE]
# these dictionaries allow for easier transition between text files and color tuples
COLOR_DICT = {
    'a' : RED,
    'b' : ORANGE,
    'c' : YELLOW,
    'd' : TAN,
    'e' : GREEN,
    'f' : LIME,
    'g' : BLUE,
    'h' : CYAN,
    'i' : PURPLE,
    'j' : HOT_PINK,
    'k' : LIGHT_PINK,
    'l' : BLACK,
    'm' : BROWN,
    'n' : DARK_GRAY,
    'o' : LIGHT_GRAY,
    'p' : WHITE,
    'q' : DEFAULT_DARK_GRAY,
    'r' : DEFAULT_WHITE
}
LETTER_DICT = {
    RED : 'a',
    ORANGE : 'b',
    YELLOW : 'c',
    TAN : 'd',
    GREEN : 'e',
    LIME : 'f',
    BLUE : 'g',
    CYAN : 'h',
    PURPLE : 'i',
    HOT_PINK : 'j',
    LIGHT_PINK : 'k',
    BLACK : 'l',
    BROWN : 'm',
    DARK_GRAY : 'n',
    LIGHT_GRAY : 'o',
    WHITE : 'p',
    DEFAULT_DARK_GRAY : 'q',
    DEFAULT_WHITE : 'r'
}
