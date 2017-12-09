  # ----------- #
  # <-- Credits --> #
  # Developed by James George#


# importing various modules required especially pygame.
import pygame
import sys
import time
import random

# Initializing pygame.

pygame.init()


# Initializing the width and height of the window to be 680 and 1250 pixels respectively.

display_height = 680
display_width = 1250


# Setting the title and dimensions of the window

pygame.display.set_caption('Catch It!')
gameDisplay = pygame.display.set_mode((display_width, display_height))


# Defining the clock to set the FPS rates
clock = pygame.time.Clock()


# Defining setText() function to display text to the screen which requires six parameters to be supplied while calling it:

# 1. The text to be displayed.
# 2. The font size.
# 3. The position in terms of X and Y coordinates in pixles where the text is to be displayed.
# 4. The background color which defaults to None if nothing are supplied.
# 6. The font type / font-family as string enclosed within double quotations which defaults to Times New Roman.

def setText(text, font_size, position, foreground_color, background_color = None, font_family="Times New Roman"):

    # Setting the font and related font features as per the parameters supplied.

    font=pygame.font.SysFont(font_family, font_size)
    text_to_display=font.render(text, 1, foreground_color, background_color)
    gameDisplay.blit(text_to_display, position)
    pygame.display.update()


# Game Play starts here!!!


def game_play():

    # Images section

    # Relatively small sized images to be placed in the main menu

    minion_image = pygame.image.load('../res/images/small_minion.jpg')

    basket_image = pygame.image.load('../res/images/small_basket.jpg')

    egg_images = ['../res/images/1.jpg', '../res/images/2.jpg', '../res/images/3.jpg', '../res/images/4.jpg', '../res/images/5.jpg', '../res/images/6.jpg', '../res/images/7.gif', '../res/images/9.jpg']

    bomb_image = pygame.image.load('../res/images/bomb.png')

    basket = pygame.image.load('../res/images/basket.jpg')

    minion = pygame.image.load('../res/images/8.jpg')

    # Initialising a boolean variable user_click to False to keep track of the user clicking any button in the main menu

    user_clicked = False

    # Boolean variables to keep track which button the user taps on the main menu

    # Whether it is the:

    # 1. Play now button

    play_clicked = False

    # 2. Instructions button

    instruction_clicked = False

    # 3. Best Scores button

    best_scores_clicked = False

    # Main Menu with 3 Buttons

    # Setting white background to the game window
    gameDisplay.fill((255, 255, 255))

    # The Title moving up and positioning itself in the required co-ordinates.
    for i in range(display_height+100, 14, -10):

        setText("Catch It!!", 140, (display_width / 2 - 340, i), (125, 20, 220), (255, 255, 255), "Algerian")
        pygame.time.wait(5)

    # Underlines
    pygame.draw.line(gameDisplay, (125, 20, 220), (display_width / 2 - 340, 165), (display_width/2+330, 165))
    pygame.draw.line(gameDisplay, (25, 120, 220), (display_width / 2 - 340, 168), (display_width/2+330, 168))
    pygame.draw.line(gameDisplay, (220, 20, 125), (display_width / 2 - 340, 170), (display_width/2+330, 170))

    gameDisplay.blit(bomb_image, (display_width/2+300, 5))

    ''' start = display_height+40
    end = 299
    value = 0

    # Setting the basket image to move from start to end.
    while start>= end:

        gameDisplay.blit(basket_image, (display_width/2-550, start))
        start-= value
        pygame.time.wait(1000)
        value+= 1
        pygame.display.update()'''

    gameDisplay.blit(basket_image, (display_width / 2 - 550, 300))

    gameDisplay.blit(minion_image, (display_width / 2 - 470, 355))

    '''q = 0
    for j in range(-20, 346):
        q+=j
        gameDisplay.blit(minion_image, (display_width/2-465, q))
        pygame.time.wait(10)'''
    # Play Button
    pygame.draw.rect(gameDisplay, (225, 10, 20), (display_width / 2 - 100, 260, 230, 100))

    # Setting Play text on the button with setText() method
    setText("Play !", 80, (530, 260), (255, 255, 255), None, "forte")
    # Instructions Button
    pygame.draw.rect(gameDisplay, (30, 220, 20), (display_width / 2 - 200, 400, 440, 100))

    # Setting Instructions text on the button with setText() method
    setText("Instructions", 80, (435, 400), (255, 255, 255), None, "forte")

    # Best Scores Button
    pygame.draw.rect(gameDisplay, (30, 22, 240), (display_width / 2 - 200, 540, 440, 100))

    # Setting Best Scores text on the button with setText() method
    setText("Best Scores", 80, (450, 540), (255, 255, 255), None, "forte")

    pygame.display.update()

    while not user_clicked:


          # (Event Loop) Keyboard and Mouse events (Checking whether the user had clicked any button)

          for event in pygame.event.get():

              # Retrieving the mouse co-ordinates (Returns a list with 2 elements i,e X and Y co-ordinates)

              mouse_cord = pygame.mouse.get_pos()

              # Checking whether the close button was tapped and if so terminate the program!
              if event.type == pygame.QUIT:

                  pygame.quit()
                  sys.exit()

              # Checking whether the mouse is within the boundaries of the respective buttons in order (Hovered / Not)
              if display_width/2-100+230>mouse_cord[0]>display_width/2-100 and 360>mouse_cord[1]>260:

                  pygame.draw.rect(gameDisplay, (150, 220, 200), (display_width / 2 - 100, 260, 230, 100))
                  setText("Play !", 80, (530, 260), (225 ,10, 20), None , "forte")

                  # Checking whether the user has clicked the play button
                  if event.type == pygame.MOUSEBUTTONDOWN:

                      user_clicked = True
                      play_clicked = True

              else:

                  pygame.draw.rect(gameDisplay, (225, 10, 20), (display_width / 2 - 100, 260, 230, 100))
                  setText("Play !", 80, (530, 260), (255, 255, 255), None, "forte")

              if display_width/2-200+440>mouse_cord[0]>display_width/2-200 and 500>mouse_cord[1]>400:

                  pygame.draw.rect(gameDisplay, (225, 100, 200), (display_width / 2 - 200, 400, 440, 100))
                  setText("Instructions", 80, (435, 400), (30, 220, 20), None, "forte")

                  # Checking whether the user has clicked the Instructions button
                  if event.type == pygame.MOUSEBUTTONDOWN:
                      user_clicked = True
                      instruction_clicked = True
              else:

                  pygame.draw.rect(gameDisplay, (30, 220, 20), (display_width / 2 - 200, 400, 440, 100))
                  setText("Instructions", 80, (435, 400), (255, 255, 255), None, "forte")

              if display_width/2-200+440>mouse_cord[0]>display_width/2-200 and 640>mouse_cord[1]>540:

                  pygame.draw.rect(gameDisplay, (16, 140, 122), (display_width / 2 - 200, 540, 440, 100))
                  setText("Best Scores", 80, (450, 540), (75, 22, 205), None, "forte")

                  # Checking whether the user has clicked the Best scores button
                  if event.type == pygame.MOUSEBUTTONDOWN:

                      user_clicked = True
                      best_scores_clicked = True

              else:

                  pygame.draw.rect(gameDisplay, (30, 22, 240), (display_width / 2 - 200, 540, 440, 100))
                  setText("Best Scores", 80, (450, 540), (255, 255, 255), None, "forte")

          clock.tick(60)


    # Instructions window
    while instruction_clicked:

        pass

    # Shows  previous best high score stored in files in the same directory where the game lies
    while best_scores_clicked:

        gameDisplay.fill((255, 0, 0))
        best_scores_clicked = False
        game_play()

    # X and Y co-ordinates of the basket.
    basket_x = display_width/2-200

    basket_y = display_height-320

    # For changing the X co-ordinate of the basket when appropriate keys are pressed.
    x_change=0

    # Random positions for eggs

    x = random.randint(0, display_width - 250)
    y = -150

    # Randomly loading Egg images

    random_eggs = pygame.image.load(egg_images[random.randint(0, 7)])

    # Game in action !!!

    while play_clicked:

        # New game window is created on clicking the play button with the same dimensions
        play_window=pygame.display.set_mode((1250,680))
        pygame.display.set_caption('Play')

        play_window.fill((255,255,255))

        play_clock=pygame.time.Clock()

        play_window.blit(random_eggs, (x, y))

        # Placing the Basket in position

        play_window.blit(basket, (basket_x, basket_y))

        # Horizontal line carrying the basket

        pygame.draw.line(play_window, (175, 115, 0), (0, display_height - 20), (display_width, display_height - 20))

        for event in pygame.event.get():

            # Pixels being moved by the basket under keystrokes (10 px)
            unit=7


            # Event Handlings
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:

                    x_change = unit

                elif event.key == pygame.K_LEFT:

                    x_change = -unit

            '''elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT or pygame.K_LEFT:

                    pass'''

        basket_x += x_change

        y+=5

        # Checking egg and basket crossover.

        if y >= basket_y:

            if x == basket_x:

               y = basket_y

        # Checking whether the egg image had crossed the floor.

        if y >= display_height+200:

            # Random positions for eggs

            x = random.randint(0, display_width - 250)
            y = -150

            # Randomly loading Egg images

            random_eggs = pygame.image.load(egg_images[random.randint(0, 7)])


        # Restricting the basket within the width of the Game window

        if basket_x <= 0 :

                basket_x = 0

        elif basket_x >= display_width-300 :

                 basket_x = display_width-300

        pygame.display.update()
        play_clock.tick(60)


if __name__ == '__main__':
    game_play()