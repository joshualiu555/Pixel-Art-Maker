from pixel import *
from icon import *
from mouse import *
from mouse_box import *
from color_box import *
from tool import *
from pygame.locals import *
from os import path
from time import sleep
from copy import deepcopy

# allows pyinstaller to read text files
import os
import sys
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
    
class Program:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pixel Art Maker")
        self.clock = pg.time.Clock()

        flags = FULLSCREEN | DOUBLEBUF
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), flags, 16)
        pg.event.set_allowed([QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYDOWN, KEYUP])

        image_folder = path.join(path.dirname(__file__), 'icons')
        self.pencil_icon = pg.image.load(path.join(image_folder, "pencil.png")).convert_alpha()
        self.eraser_icon = pg.image.load(path.join(image_folder, "eraser.png")).convert_alpha()
        self.trashcan_icon = pg.image.load(path.join(image_folder, "trashcan.png")).convert_alpha()
        self.square_icon = pg.image.load(path.join(image_folder, "square.png")).convert_alpha()
        self.line_icon = pg.image.load(path.join(image_folder, "line.png")).convert_alpha()
        self.bucket_icon = pg.image.load(path.join(image_folder, "bucket.png")).convert_alpha()
        self.undo_icon = pg.image.load(path.join(image_folder, "undo.png")).convert_alpha()
        self.redo_icon = pg.image.load(path.join(image_folder, "redo.png")).convert_alpha()
        self.export_icon = pg.image.load(path.join(image_folder, "export.png")).convert_alpha()
        self.images = [[(self.pencil_icon, "pencil"), (self.eraser_icon, "eraser"), (self.trashcan_icon, "trashcan")],
                       [(self.square_icon, "square"), (self.line_icon, "line"), (self.bucket_icon, "bucket")],
                       [(self.undo_icon, "undo"), (self.redo_icon, "redo"), (self.export_icon, "export")]]

        self.all_sprites = pg.sprite.Group()
        self.pixel_list = []
        self.icon_list = []
        self.mouse_box_list = []
        self.color_box_list = []

        self.board = []
        self.undo = []
        self.redo = []

        self.current_icon = "pencil"
        self.mouse = Mouse(1, BLACK)
        self.mouse_down = False

        self.square_x1, self.square_y1 = None, None
        self.square_x2, self.square_y2 = None, None
        self.line_x1, self.line_y1 = None, None
        self.line_x2, self.line_y2 = None, None

        self.running = True

    # creates sprite lists and sprite groups
    def new(self):
        # initializes the board based on the save file
        with open('board.txt', 'r') as file:
            for line in file:
                row = []
                for letter in line:
                    row.append(letter)
                self.board.append(row)
        self.undo.append(deepcopy(self.board))
        file.close()

        for x in range(int(NUM_ROWS)):
            row = []
            for y in range(int(NUM_COLUMNS)):
                pixel = Pixel(COLOR_DICT[self.board[x][y]], x, y)
                row.append(pixel)
            self.pixel_list.append(row)

        for x in range(3):
            for y in range(3):
                icon = Icon(self.images[x][y][0], self.images[x][y][1], y, x, 40)
                self.icon_list.append(icon)

        for box_count in range(10):
            mouse_box = mouseBox(box_count, 10)
            self.mouse_box_list.append(mouse_box)

        for x in range(4):
            for y in range(4):
                color = ColorBox(COLOR_GRID[x][y], y, x, 5)
                self.color_box_list.append(color)

        # initializes the current selections based on save file
        with open('selection.txt', 'r') as file:
            index = int(file.readline())
            self.current_icon = self.icon_list[index].tool_name
            self.icon_list[index].selected = True
            index = int(file.readline())
            color = COLOR_LIST[index]
            self.color_box_list[index].selected = True
            size = int(file.readline())
            self.mouse = Mouse(size, color)
        file.close()

        for row in self.pixel_list:
            for pixel in row:
                self.all_sprites.add(pixel)
        for color_box in self.color_box_list:
            self.all_sprites.add(color_box)
        for mouse_size in self.mouse_box_list:
            self.all_sprites.add(mouse_size)
        for icon in self.icon_list:
            self.all_sprites.add(icon)
        self.all_sprites.add(self.mouse)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            # checks if the mouse is being clicked
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_down = True
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_down = False
                # adds current board state to the undo stack
                if self.mouse.on_board and (self.current_icon == "pencil" or self.current_icon == "eraser" or self.current_icon == "bucket"
                                            or self.current_icon == "square" or self.current_icon == "line"):
                    self.undo.append(deepcopy(self.board))
                    self.redo.clear()
            if event.type == pg.KEYDOWN:
                # changes the mouse size
                if event.key == pg.K_RIGHT and self.mouse.size < 10:
                    self.mouse.change_size(self.mouse.size + 1)
                elif event.key == pg.K_LEFT and self.mouse.size > 1:
                    self.mouse.change_size(self.mouse.size - 1)
                # quits the program
                elif event.key == pg.K_ESCAPE:
                    self.running = False
        if not self.running:
            # saves the current board state and selections
            with open('board.txt', 'w') as file:
                for line in self.board:
                    row = ''.join(line)
                    file.write(row)
            file.close()
            with open('selection.txt', 'w') as file:
                for index in range(len(self.icon_list)):
                    if self.icon_list[index].selected:
                        file.write(str(index) + "\n")
                        break
                for index in range(len(self.color_box_list)):
                    if self.color_box_list[index].selected:
                        file.write(str(index) + "\n")
                file.write(str(self.mouse.size) + "\n")

    def update(self):
        if self.mouse_down and self.mouse.on_board:
            if self.current_icon == "trashcan":
                trashcan(self.pixel_list, self.board)
                self.undo.clear()
                self.redo.clear()
            elif self.current_icon == "export":
                export(self.screen)
            elif self.current_icon == "bucket":
                bucket(self.pixel_list, self.mouse, self.board)
            elif self.current_icon == "square":
                # avoids multiple clicks due to FPS
                sleep(0.1)
                # selected pixel
                selected_pixel = None
                flag = False
                for row in self.pixel_list:
                    for pixel in row:
                        if self.mouse.rect.colliderect(pixel.rect):
                            selected_pixel = pixel
                            flag = True
                            break
                    if flag:
                        break
                # first pixel selected
                if self.square_x1 is None and self.square_y1 is None:
                    self.square_x1, self.square_y1 = selected_pixel.x, selected_pixel.y
                    selected_pixel.change_color(self.mouse.color)
                    self.board[selected_pixel.x][selected_pixel.y] = LETTER_DICT[self.mouse.color]
                # second pixel selected
                else:
                    self.square_x2, self.square_y2 = selected_pixel.x, selected_pixel.y
                    # swaps pixels so first is top left and second is bottom right
                    if self.square_x1 > self.square_x2:
                        temp = self.square_x1
                        self.square_x1 = self.square_x2
                        self.square_x2 = temp
                    if self.square_y1 > self.square_y2:
                        temp = self.square_y1
                        self.square_y1 = self.square_y2
                        self.square_y2 = temp
                    # draws the pixels
                    for top in range(self.square_x1, self.square_x2 + 1):
                        self.pixel_list[top][self.square_y1].change_color(self.mouse.color)
                        self.board[top][self.square_y1] = LETTER_DICT[self.mouse.color]
                    for bottom in range(self.square_x1, self.square_x2 + 1):
                        self.pixel_list[bottom][self.square_y2].change_color(self.mouse.color)
                        self.board[bottom][self.square_y2] = LETTER_DICT[self.mouse.color]
                    for left in range(self.square_y1, self.square_y2 + 1):
                        self.pixel_list[self.square_x1][left].change_color(self.mouse.color)
                        self.board[self.square_x1][left] = LETTER_DICT[self.mouse.color]
                    for right in range(self.square_y1, self.square_y2 + 1):
                        self.pixel_list[self.square_x2][right].change_color(self.mouse.color)
                        self.board[self.square_x2][right] = LETTER_DICT[self.mouse.color]
                    # reset the pixel selections
                    self.square_x1, self.square_y1 = None, None
                    self.square_x2, self.square_y2 = None, None
            elif self.current_icon == "line":
                sleep(0.1)
                selected_pixel = None
                flag = False
                for row in self.pixel_list:
                    for pixel in row:
                        if self.mouse.rect.colliderect(pixel.rect):
                            selected_pixel = pixel
                            flag = True
                            break
                    if flag:
                        break
                if self.line_x1 is None and self.line_y1 is None:
                    self.line_x1, self.line_y1 = selected_pixel.x, selected_pixel.y
                    selected_pixel.change_color(self.mouse.color)
                else:
                    self.line_x2, self.line_y2 = selected_pixel.x, selected_pixel.y
                    if self.line_x1 == self.line_x2:
                        if self.line_y1 > self.line_y2:
                            temp = self.line_y1
                            self.line_y1 = self.line_y2
                            self.line_y2 = temp
                        for column in range(self.line_y1, self.line_y2):
                            self.pixel_list[self.line_x2][column + 1].change_color(self.mouse.color)
                            self.board[self.line_x2][column] = LETTER_DICT[self.mouse.color]
                        self.line_x1, self.line_y1 = None, None
                        self.line_x2, self.line_y2 = None, None
                    elif self.line_y1 == self.line_y2:
                        if self.line_x1 > self.line_x2:
                            temp = self.line_x1
                            self.line_x1 = self.line_x2
                            self.line_x2 = temp
                        for row in range(self.line_x1, self.line_x2):
                            self.pixel_list[row + 1][self.line_y1].change_color(self.mouse.color)
                            self.board[row][self.line_y2] = LETTER_DICT[self.mouse.color]
                        self.line_x1, self.line_y1 = None, None
                        self.line_x2, self.line_y2 = None, None
            # every selected state in "undo" is pushed to "redo" and vice versa
            elif self.current_icon == "undo":
                if self.undo:
                    # avoids multiple clicks due to FPS
                    sleep(0.1)
                    # deep copies to avoid editing previous states (python sets objects by reference)
                    temp = deepcopy(self.undo.pop())
                    self.redo.append(deepcopy(temp))
                    for x in range(NUM_ROWS):
                        for y in range(NUM_COLUMNS):
                            self.pixel_list[x][y].change_color(COLOR_DICT[temp[x][y]])
                            self.board[x][y] = temp[x][y]
            elif self.current_icon == "redo":
                if self.redo:
                    sleep(0.1)
                    temp = deepcopy(self.redo.pop())
                    self.undo.append(deepcopy(temp))
                    for x in range(NUM_ROWS):
                        for y in range(NUM_COLUMNS):
                            self.pixel_list[x][y].change_color(COLOR_DICT[temp[x][y]])
                            self.board[x][y] = temp[x][y]
            else:
                # checks for collision with pixel
                for row in self.pixel_list:
                    for pixel in row:
                        if self.mouse.rect.colliderect(pixel.rect):
                            if self.current_icon == "pencil":
                                pencil(pixel, self.mouse.color, self.board)
                            elif self.current_icon == "eraser":
                                eraser(pixel, self.board)

        for color_box in self.color_box_list:
            if self.mouse_down and color_box.rect.collidepoint(self.mouse.rect.topleft):
                self.mouse.change_color(color_box.color)
                # sets other color boxes to false and the selected one to true
                for other_color_box in self.color_box_list:
                    other_color_box.selected = False
                color_box.selected = True

        for icon in self.icon_list:
            # uses topleft because the mouse rect could be really big, so it only uses one point on the mouse
            if self.mouse_down and icon.rect.collidepoint(self.mouse.rect.topleft):
                self.current_icon = icon.tool_name
                # sets other icons to false and the selected one to true
                for other_icon in self.icon_list:
                    other_icon.selected = False
                icon.selected = True
                # if you are in the middle of selecting a shape but switch to another icon, reset the selection
                if self.current_icon != "square":
                    self.square_x1, self.square_y1 = None, None
                    self.square_x2, self.square_y2 = None, None
                elif self.current_icon != "line":
                    self.line_x1, self.line_y1 = None, None
                    self.line_x2, self.line_y2 = None, None

        mouse_box_index = 0
        while mouse_box_index < self.mouse.size:
            self.mouse_box_list[mouse_box_index].selected = True
            mouse_box_index += 1
        while mouse_box_index < 10:
            self.mouse_box_list[mouse_box_index].selected = False
            mouse_box_index += 1

        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        for color_box in self.color_box_list:
            color_box.draw_circle(self.screen)
        for icon in self.icon_list:
            icon.draw_border(self.screen)
        pg.display.update()


pixelart = Program()
pixelart.new()
while pixelart.running:
    pixelart.run()

pg.quit()
