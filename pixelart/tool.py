import pygame as pg
from constants import *
from datetime import datetime

def trashcan(pixel_list, board):
    for x in range(NUM_ROWS):
        for y in range(int(NUM_COLUMNS)):
            # allows for alternating gray and white
            if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                pixel_list[x][y].change_color(DEFAULT_DARK_GRAY)
                board[x][y] = LETTER_DICT[DEFAULT_DARK_GRAY]
            else:
                pixel_list[x][y].change_color(DEFAULT_WHITE)
                board[x][y] = LETTER_DICT[DEFAULT_WHITE]

def export(screen):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    subscreen = screen.subsurface((400, 0, 800, 800))
    pg.image.save(subscreen, 'screenshots/' + formatted_time + '.png')

def bucket(pixel_list, mouse, board):
    # start filling from here
    selected_pixel = None
    flag = False
    for row in pixel_list:
        for pixel in row:
            if mouse.rect.colliderect(pixel.rect):
                selected_pixel = pixel
                flag = True
                break
        if flag:
            break
    visited = []
    for i in range(int(NUM_ROWS)):
        row = []
        for j in range(int(NUM_COLUMNS)):
            row.append(False)
        visited.append(row)
    # equivalent to recursion stack, but allows for iterative floodfill to prevent segmentation fault
    bucket_stack = [(selected_pixel.x, selected_pixel.y)]
    start_color = selected_pixel.color
    while len(bucket_stack) > 0:
        info = bucket_stack.pop()
        x, y = info[0], info[1]
        # out of bounds
        if x < 0 or y < 0 or x == int(NUM_ROWS) or y == int(NUM_COLUMNS):
            continue
        if visited[x][y]:
            continue
        pixel = pixel_list[x][y]
        # uses DEFAULT_DARK_GRAY AND DEFAULT_WHITE because it prevents filling pixels that were intentionally gray or white by the user
        if pixel.color != DEFAULT_DARK_GRAY and pixel.color != DEFAULT_WHITE and pixel.color != start_color:
            continue
        if pixel.color == mouse.color:
            continue
        visited[x][y] = True
        pixel.change_color(mouse.color)
        board[x][y] = LETTER_DICT[mouse.color]
        bucket_stack.append((x + 1, y))
        bucket_stack.append((x - 1, y))
        bucket_stack.append((x, y + 1))
        bucket_stack.append((x, y - 1))

def pencil(pixel, color, board):
    pixel.change_color(color)
    x, y = pixel.x, pixel.y
    board[x][y] = LETTER_DICT[color]

def eraser(pixel, board):
    x, y = pixel.x, pixel.y
    # allows for alternating gray and white
    if (pixel.x % 2 == 0 and pixel.y % 2 == 0) or (pixel.x % 2 == 1 and pixel.y % 2 == 1):
        pixel.change_color(DEFAULT_DARK_GRAY)
        board[x][y] = LETTER_DICT[DEFAULT_DARK_GRAY]
    else:
        pixel.change_color(DEFAULT_WHITE)
        board[x][y] = LETTER_DICT[DEFAULT_WHITE]
