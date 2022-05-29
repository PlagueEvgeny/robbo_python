import pygame
import time
import random

pygame.init()
pygame.display.set_caption("Snake game by Robbo")


pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(-1)



black=(0, 0, 0)
white=(255, 255, 255)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow = (255, 255, 102)

dis_width = 800
dis_height = 600

dis=pygame.display.set_mode((dis_width, dis_height))

snake_block = 10


font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)

def your_score(score):
    value = score_font.render('Your Score: ' + str(score), True, yellow)
    dis.blit(value, [0, 0])

def apple_food(x, y):
    apple = pygame.image.load('image/apple.png')
    apple_rect = pygame.transform.scale(apple, (snake_block, snake_block))
    dis.blit(apple_rect, [x, y])
    
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def gameLoop():
    snake_speed = 30
    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Lenght_of_snake = 1

    clock = pygame.time.Clock()
    
    game_close = False
    game_over = False

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10

    while not game_over:
        
        while game_close == True:
            dis.fill(white)
            message('Вы проиграли! Нажмите Q-Выход или C-Играть заново', red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()



            

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            ## K_LEFT K_RIGHT K_UP K_DOWN
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

                elif event.key == pygame.K_o:
                    snake_speed += 10
                    
                elif event.key == pygame.K_i:
                    snake_speed -= 10

        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)
        
        apple_food(foodx, foody)
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Lenght_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Lenght_of_snake - 1)
        
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10

            Lenght_of_snake += 1

        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameLoop()
