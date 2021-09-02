# Pixel Art Maker
Program Purpose: Allows the user to make pixel art 

Features: 16 colors, pencil, eraser, trashcan, square, line, bucket, undo / redo, export, different mouse size

Language: Python and Pygame

[Link to Project](https://replit.com/@joshualiu555/Pixel-Art-Maker#main.py)

[Inspired by pixilart](https://www.pixilart.com)

![14:31:58](https://user-images.githubusercontent.com/53412192/120903395-8435f280-c60b-11eb-951d-b96d30303164.png)

## Class Overview
###### Pixel
Attributes: Color, position

Methods: Change color

###### Icon - Pencil, eraser, trashcan, etc.
Attributes: Image name, tool / icon name, position

Methods: Draw border

###### Mouse
Attributes: Size, color

Methods: Update - Highlights current pixel, becomes transparent if it is not on the board, changes cursor to diamond if it is on the board

###### Mouse Box - Boxes that show the size of the mouse
Attributes: Position

Methods: Update - Sets to visible or transparent depending on mouse size

###### Color Box - 16 of these that each represent a color presented in a grid
Attributes: Color, position

Methods: Draw circle - draws a circle in the box if it is selected

###### Tool - Each icons individual function when called
Trashcan: Erases the whole board and resets the alternating gray and white grid

Export: Takes a picture of the canvas and saves it to a screenshot folder

Bucket: Fills the surrounding area with a color

Pencil: Changes a pixel's color

Eraser: Resets a pixel's color to its original gray or white

Square: Creates a square based on 2 selected points (Bugs - Sometimes doesn't respond, when undoing, the second point is erased too)

Line: Creates a line based on 2 selected points (Bugs - same as square)

Undo: Reverses the board to the previous state (Bugs - takes 2 clicks for the first undo)

Redo: Restores the board to the state you just had (Bugs - same as undo)

## How the program works - main.py
###### new() - initializing everything
The board and current selections (tool, mouse size, color) are created using a text file that allows for saving previous work.

Each class has its own sprite group and list containing instance

###### run() - performs every essential part of the game loop

###### events() - checks for mouse or keyboard events
Checks for escape key to exit. If it is, the program saves the current board and selections.

Checks if the mouse is being clicked. Everytime the mouse is released, a new board state is pushed to the undo stack

Checks for arrow keys to change the mouse size

###### update() - hanges the board and current selection
Checks if there the mouse and pixel collide. If they do, they perform the necessary function based on the current tool.

Checks if a color box or tool has been selected. 

Updates the amount of mouse boxes to be shown.

Updates every sprite (polymorphism)

###### draw() - fills the screen, draws the sprites and borders, updates the display

###### program instance - creates the program

## Install as an executable file
Open the terminal / command line

pip install pyinstaller

Open up a terminal / command line inside the directory

pyinstaller --add-data "board.txt:." --add-data "reset.txt:." --add-data "selections.txt:." --add-data "icons:icons" --add-data "screenshots:screenshots" main.py

Go to dist and select main.exe

Enjoy and happy coding :)
