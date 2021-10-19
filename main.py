import functools

import pygame
import math
import path
import random
import time
import itertools

pygame.init()
paused = False
red = pygame.sprite.Group()
green = pygame.sprite.Group()
dice = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
size = (600, 800)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
dice_number = 0
pygame.display.set_caption("Ludo")
board = pygame.image.load('Assets/board.png')
pygame.display.set_icon(board)
carryOn = True
clock = pygame.time.Clock()
current_position = 0
font = pygame.font.Font('Assets/Montserrat-Regular.ttf', 25)
text = font.render('PAUSE', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (300, 230)
object_path = {}
# <-------------Music----------->
pygame.mixer.init()
pygame.mixer.music.load('Assets/Desmeon - Hellcat [NCS Release].mp3')

pygame.mixer.music.play(0)
all_position_numbers = itertools.cycle([1, 2, 3])


# <-------------Music----------->

class Disc(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load('Assets/Dice/D1.png').convert_alpha(), (50, 50))
        # self.image1 = pygame.transform.smoothscale(pygame.image.load('Assets/Dice/disc1.png').convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.size = (300, 300)
        # self.rect.x, self.rect.y = (150, 680)
        # self.rect = self.image.get_rect()
        # # self.rect.size
        self.rect.x, self.rect.y = (270, 720)

    def clicked(self):
        global dice_number
        global current_position
        if math.dist((self.rect.x, self.rect.y), pygame.mouse.get_pos()) <= 40:
            # self.image = pygame.transform.smoothscale(pygame.image.load('Assets/Dice/D2.png').convert_alpha(),
            #                                           (50, 50))
            # print("dice clicked")
            dice_number = random.randint(1, 6)
            self.image = pygame.transform.smoothscale(
                pygame.image.load(f'Assets/Dice/D{str(dice_number)}.png').convert_alpha(),
                (50, 50))
            current_position = next(all_position_numbers)


class Pawn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.collision_targets = None
        self.positionNumber = 0  # changed to 1
        self.dx = 0
        self.dy = 0
        self.inMotion = True
        self.moved = False
        self.image = None
        self.path = None
        self.color = None
        all_sprites.add(self)
        self.radius = 2
        self.collided = False
        self.starPosition = None
        self.starPositionNumber = 0
        self.starPath = {}
        self.t = 0
        self.number = 0
        self.isMoving = False
        self.globalPosition = 0

    def clicked(self):
        global dice_number
        # print('dice gamers')
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(self.number, 'selfnumber,')
            print(current_position, 'current_position')
            if math.dist((self.path[self.positionNumber]),
                         pygame.mouse.get_pos()) <= 40 and self.number == current_position:
                if self.t == 0 and dice_number == 6:
                    self.t += 1
                elif self.t > 0:
                    self.t += dice_number
                    self.globalPosition += dice_number
                    self.collided = False
                    collision_check(self.color, self)

    def movement2(self):
        global object_path
        if not self.collided:
            # print(self.rect.x, self.rect.y)
            # print(movement_no)
            # print(movement_no)
            # print(self.path[0])
            # pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            x_complete = y_complete = False
            # print(t)
            point = self.path[self.positionNumber]
            # print(self.positionNumber)
            # print(self.rect.x)
            # print(self.rect.y)
            if self.rect.y < point[1]:
                self.rect.y += 1
            elif self.rect.y > point[1]:
                self.rect.y -= 1
            else:
                y_complete = True

            if self.rect.x < point[0]:
                self.rect.x += 1
            elif self.rect.x > point[0]:
                self.rect.x -= 1
            else:
                x_complete = True
            if x_complete and y_complete:
                if self.positionNumber != self.t:
                    self.isMoving = True
                    # self.collision()
                    self.positionNumber += 1

                    # self.collision()  # checking for collision every step

                    self.starPositionNumber += 1
                else:
                    self.isMoving = False
                #     if self.positionNumber in [14, 28, 42]:
                #         self.starPosition = [1, 2, 3, 4][self.starPosition % 4]
                #         # print(self.starPositionNumber, self.color)
                #         self.starPositionNumber = 0
                #     self.starPath[self] = (self.starPosition, self.starPositionNumber)
                #     object_path.append({self: (self.starPosition, self.starPositionNumber)})
                #     # print(self.starPath)
                # else:
                #     # print('gelly')
                #     self.starPath[self] = (self.starPosition, self.starPositionNumber)

    # def collision(self):
    #     if self.globalPosition ==
    #     pass
# d1 = red:(), blue:()
# ((red1, red2),(blie1,),(ddkjd,sdfsdf))
# (red1, red2,blue1,ddkjd)

    # print(self.starPath.get(self))
    # print(object_path)
    # print(self.starPath)
    # if self.starPath in object_path:
    #     object_path.remove(self.starPath)
    # # print(object_path)
    # collide = pygame.sprite.spritecollide(self, green, False)
    # # object_path - self.starPath
    # for i in object_path:
    #     for j in i.values():
    #         # print(self.starPath.get(self), 'uyubhbuhbhbuhbbhbhubuubbubu', j)
    #         if self.starPath.get(self) == j:
    #             i.keys()

    # self.positionNumber = 56

    # print(self.starPath.values())
    # if self.starPath.values() in object_path:
    #     print()
    #     print(self.starPath.keys())
    #     pass

    # def update(self, j):
    #     global l
    #     global x
    #     x_complete = y_complete = False
    #     self.collided = False
    #     self.positionNumber = 1
    #     x = 0
    #     # print(self.path[0])
    #
    #     point = self.path[0]
    #     # print(point[1], self.rect.y)
    #     if self.rect.y < point[1]:
    #         self.rect.y += 1
    #     elif self.rect.y > point[1]:
    #         self.rect.y -= 1
    #     else:
    #         y_complete = True
    #     if self.rect.x < point[0]:
    #         self.rect.x += 1
    #     elif self.rect.x > point[0]:
    #         self.rect.x -= 1
    #     else:
    #         x_complete = True
    #
    #     if x_complete and y_complete:
    #         l.remove(j)
    #         pass

    # def collision(self):
    #     # collision_targets = [[green1.globalPosition, "green1"], [green2.globalPosition, "green2"],
    #     #                      [green3.globalPosition, "green3"], [green4.globalPosition, "green4"]]
    #     collision_targets = self.collision_targets
    #
    #     for target_position, target_name in self.collision_targets:
    #         if self.globalPosition == target_position:
    #             print(target_name)
    #             eval(f"{target_name}.home()")  # Will go back to to square 1
    #
    # def home(self):
    #     """This function is helps to go back to home"""
    #     self.positionNumber = 0
    #     self.globalPosition = 1
    #     self.t = 0


class RedPawn(Pawn):
    def __init__(self, start_position):
        super().__init__()
        self.color = 'red'
        self.image = pygame.image.load('Assets/Untitled (2).png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_position  # remove this to start from the beginning
        self.path = {0: start_position} | path.red
        self.number = 1
        self.globalPosition = 1
        # self.collision_targets = [[green1.globalPosition, "green1"], [green2.globalPosition, "green2"],
        #                           [green3.globalPosition, "green3"], [green4.globalPosition, "green4"]]

    def home(self):
        """This function is helps to go back to home"""
        self.positionNumber = 0
        self.globalPosition = 1
        self.t = 0


class BluePawn(Pawn):
    def __init__(self, start_position):
        super().__init__()
        self.color = 'blue'
        self.image = pygame.image.load('Assets/untitled (1).png')
        self.path = {0: start_position, 1: (780, 0), 2: (0, 0), 3: (100, 300), 4: (100, 100)}


class YellowPawn(Pawn):
    def __init__(self, start_position):
        super().__init__()
        self.color = 'yellow'
        self.image = pygame.image.load('Assets/untitled (1).png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_position
        self.path = {0: start_position} | path.yellow
        self.number = 3
        self.globalPosition = 27

    # def collision(self):
    #     collision_targets = [[green1.globalPosition, "green1"], [green2.globalPosition, "green2"],
    #                          [green3.globalPosition, "green3"], [green4.globalPosition, "green4"]]
    #
    #     for target_position, target_name in collision_targets:
    #         if self.globalPosition == target_position:
    #             print(target_name)
    #             eval(f"{target_name}.home()")  # Will go back to to square 1

    def home(self):
        """This function is helps to go back to home"""
        self.positionNumber = 0
        self.globalPosition = 27
        self.t = 0


class GreenPawn(Pawn):
    def __init__(self, start_position):
        super().__init__()
        self.color = 'green'
        self.image = pygame.image.load('Assets/untitled (1).png')
        self.rect = self.image.get_rect()
        self.rect.size = 10, 10
        self.rect.x, self.rect.y = start_position
        self.path = {0: start_position} | path.green
        self.starPosition = 2
        self.number = 2  # Each color has a number and for green it is 2
        self.globalPosition = 14

    def home(self):
        # self.rect.x, self.rect.y = self.startPosition
        self.positionNumber = 0
        self.globalPosition = 14
        self.t = 0

    def collision(self):
        pass
        # print("My position number for green is," , self.globalPosition)
        # collision_targets = [[red1.globalPosition, "red1"], [red2.globalPosition, "red2"],
        #                      [red3.globalPosition, "red3"], [red4.globalPosition, "red4"]]
        #
        # for target_position, target_name in collision_targets:
        #     if self.globalPosition == target_position:
        #         print(target_name)
        #         eval(f"{target_name}.home()")  # Will go back to to square 1


# <-----------------------Object Creation--------------->
red1 = RedPawn((140, 138 + 76))
red2 = RedPawn((140, 59 + 76))
red3 = RedPawn((60, 59 + 76))
red4 = RedPawn((60, 138 + 76))
green1 = GreenPawn((419, 60 + 76))
green2 = GreenPawn((419, 139 + 76))
green3 = GreenPawn((501, 60 + 76))
green4 = GreenPawn((501, 139 + 76))
yellow1 = YellowPawn((501, 496))
yellow2 = YellowPawn((419, 496))
yellow3 = YellowPawn((501, 573))
yellow4 = YellowPawn((419, 573))

all_sprites.add(red1, red2, red3, red4, green1, green2, green3, green4, yellow1, yellow2, yellow3, yellow4)
# print(all_sprites.sprites())
d = Disc()
dice.add(d)


# print(red.sprites())
# print(green.sprites())
# all_sprites = pygame.sprite.Group()
# print(all_sprites)
# <-----------------------Object Creation--------------->

def mute():
    if pygame.mixer.music.get_volume() != 0:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume((volume_variable - 210) / 180)


def pause():
    global paused
    if pygame.mixer.music.get_busy() and not paused:
        paused = True
    else:
        paused = False


volume_variable = 280


def volume_slider(x, y):
    global volume_variable
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, 180, 20), 0, 10)
    if pygame.mouse.get_pressed(num_buttons=3)[0] and 390 > pygame.mouse.get_pos()[0] > 210 and math.dist(
            (volume_variable, y + 10), pygame.mouse.get_pos()) <= 40:
        if volume_variable != pygame.mouse.get_pos()[0]:
            volume_variable = pygame.mouse.get_pos()[0]
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, volume_variable - x, 20), 0, 10)
            pygame.draw.circle(screen, (0, 0, 0), (volume_variable, y + 10), 15)
            pygame.mixer.music.set_volume((volume_variable - x) / 180)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, volume_variable - x, 20), 0, 10)
    pygame.draw.circle(screen, (0, 0, 0), (volume_variable, y + 10), 15)


def pause_menu():
    pygame.draw.rect(screen, (24, 24, 24), pygame.Rect(200, 200, 200, 300), 0, 10)
    screen.blit(text, textRect)
    volume_slider(210, 350)


l = []
x = 2

a = 0


# l []
def collision_check(color, currently_moving):
    # sprites = [red1, red1, red2, red3, green1, green2, green3, green4, yellow1, yellow2, yellow3, yellow4]
    # sprites = [red1.globalPosition, red2.globalPosition, red3.globalPosition, red4.globalPosition]
    #
    # # sprite_speed = [red1, red2, red3, green1, green2, green3, green4, yellow1, yellow2, yellow3, yellow4]
    # for i in sprites:
    #
    #
    # try:
    #     sprites.index()
    sprites = {'red': (red1, red2, red3, red4), 'green': (green1, green2, green3, green4), 'yellow': (yellow1, yellow2)}
    sprites.pop(color)
    collision_targets = (sprites.values())  # list of tuples of different colors

    for i in collision_targets:
        for j in i:
            print(j)
            if currently_moving.globalPosition == j.globalPosition and j.globalPosition not in [1, 9, 14, 22, 27, 35, 40, 48]:
                j.home()



# sprites = {'red': (red1, red2, red3, red4), 'green': (green1, green2, green3, green4), 'yellow':(yellow1,)}
global_position_list = [red1.globalPosition, red2.globalPosition, red3]
globals = []
# collision_check(sprites)


while carryOn:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (21, 19, 21), pygame.Rect(0, 0, size[0], 75))
    pygame.draw.rect(screen, (21, 19, 21), pygame.Rect(0, size[1] - 100, size[1], 100))

    screen.blit(board, (0, 75))
    # pygame.draw.circle(screen, (255, 0, 0), (285, 750), 25)
    pygame.draw.rect(screen, (24, 24, 24), pygame.Rect(360, 0, 300, 75), 0, 10)
    pygame.draw.rect(screen, (24, 24, 24), pygame.Rect(-60, 0, 300, 75), 0, 10)
    # red.draw(screen)
    # green.draw(screen)
    all_sprites.draw(screen)
    dice.draw(screen)

    red1.movement2()
    red2.movement2()
    red3.movement2()
    red4.movement2()
    green1.movement2()
    green2.movement2()
    green3.movement2()
    green4.movement2()
    yellow1.movement2()
    yellow2.movement2()
    yellow3.movement2()
    yellow4.movement2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            red1.clicked()
            red2.clicked()
            red3.clicked()
            red4.clicked()
            green1.clicked()
            green2.clicked()
            green3.clicked()
            green4.clicked()
            yellow1.clicked()
            yellow2.clicked()
            yellow3.clicked()
            yellow4.clicked()
            d.clicked()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()
            elif event.key == pygame.K_m:
                mute()
            elif event.key == pygame.K_DOWN:
                volume_variable = volume_variable - 18
            elif event.key == pygame.K_UP:
                volume_variable = volume_variable + 18

    if paused:
        pause_menu()
    # collide_check = pygame.sprite.groupcollide(green, red, False, False)
    # print(collide_check)
    # for i in collide_check:
    #     i.update(0)
    #     l.append(i)
    # print(l, 'stupid')

    # if l:
    #     for j in l:
    #         j.update(j)
    pygame.display.flip()
    # Limit to 60 frames per second
    clock.tick(60)
pygame.quit()
