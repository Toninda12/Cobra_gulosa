# inicial config

import pygame
import random

from pygame.examples.go_over_there import event

pygame.init()
pygame.display.set_caption("titanoboa sinistra")
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#colors rgb
black = (0, 0, 0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)

#parameters of the snake
square_size = 20
game_speed = 15

def food_generator():
    food_x = round (random.randrange(0, width - square_size) / 20.0) * 20.0
    food_y = round (random.randrange(0, height - square_size) / 20.0) * 20.0
    return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, green,[food_x,food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white,[pixel[0], pixel[1], size, size] )

def draw_pontuation(pontuation):
    font = pygame.font.SysFont("Helvetica", 35)
    text = font.render(f"Points: {pontuation}", False, red)
    screen.blit(text, [1,1])

def speed_selector(Key):
    if Key == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
    elif Key == pygame.K_UP:
        speed_x = 0
        speed_y = -square_size
    elif Key == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0
    elif Key == pygame.K_LEFT:
        speed_x = -square_size
        speed_y = 0

    return speed_x, speed_y

def run_game():
    end_game = False

    x = width / 2
    y = height / 2

    snake_size = 1
    pixels = []

    speed_x = 0
    speed_y = 0

    food_x, food_y = food_generator()

    while not end_game:
        screen.fill(black)


        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                end_game = True
            elif Event.type == pygame.KEYDOWN:
                speed_x, speed_y = speed_selector(Event.key)

        # draw objects in the screen
        # food
        draw_food(square_size, food_x, food_y)

        #update snake position
        if x < 0 or x >= width or y < 0 or y >= height:
            end_game = True

        x += speed_x
        y += speed_y

        # snake
        pixels.append([x,y])
        if len(pixels) > snake_size:
            del pixels[0]

        # if the snake hit its own body
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                end_game = True

        draw_snake(square_size, pixels)

        # pontuation
        draw_pontuation(snake_size - 1)


        #screen update
        pygame.display.update()

        #create new food
        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = food_generator()

        clock.tick(game_speed)
# create infinite loop






#create logic
#what happens
#snake strikes parede
#snake strike snake

# user interactions
# fechou a tela
# apertou as teclas para mover
run_game()