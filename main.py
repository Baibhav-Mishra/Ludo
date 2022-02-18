import functools
import pygame
import math
import path
import random
import cred
import time
import mysql.connector
con = mysql.connector.connect(host=cred.host, password=cred.password, user=cred.user, database=cred.database)
cursor = con.cursor()
cursor.execute("select * from info2")
results = cursor.fetchone()
no_of_players = results[0]
player1 = results[1]
player2 = results[2]
player3 = results[3]

player4 = results[4]
import itertools
pygame.init()
paused = False
red = pygame.sprite.Group()
green = pygame.sprite.Group()
dice = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
size = (600, 800)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
dice_number = 1
pygame.display.set_caption("Ludo")
board = pygame.image.load('Assets/board.png')
pawn1_avatar_image = pygame.image.load('Assets/Untitled (2).png')
pawn2_avatar_image = pygame.image.load('Assets/green.png')
pawn3_avatar_image = pygame.image.load('Assets/blue.png')
pawn4_avatar_image = pygame.image.load('Assets/yellow.png')
colour_already_moved = False
pygame.display.set_icon(board)
carryOn = True
clock = pygame.time.Clock()
current_position = 0
font = pygame.font.Font('Assets/Montserrat-Medium.ttf', 25)
text = font.render('PAUSE', True, (255, 255, 255))
pawn1_username = font.render('Red_Username', True, (255, 255, 255))

def textprint(text, location, color):
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = location
    screen.blit(text_render, text_rect)

pawn2_username = font.render('Green_Username', True, (255, 255, 255)).get_rect()
pawn3_username = font.render('Blue_Username', True, (255, 255, 255)).get_rect()
pawn4_username = font.render('Yellow_Username', True, (255, 255, 255)).get_rect()
textRect = text.get_rect()
textRect.center = (300, 230)
object_path = {}
dice_clicked = bool()
pawn_clicked = True
# <-------------Music----------->
pygame.mixer.init()
pygame.mixer.music.load('Assets/Desmeon - Hellcat [NCS Release].mp3')

pygame.mixer.music.play(-1)




# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root1234",
#   database="Lud"
# )
#
# mycursor = mydb.cursor()
#
#
#
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
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
        self.rect.x, self.rect.y = (275, 695)
        self.overlap = False

    def clicked(self):
        global dice_number
        global current_position
        global dice_clicked
        global pawn_clicked
        global colour_already_moved
        if math.dist((self.rect.x + 35, self.rect.y+ 35), pygame.mouse.get_pos()) <= 39:
            # self.image = pygame.transform.smoothscale(pygame.image.load('Assets/Dice/D2.png').convert_alpha(),
            #                                           (50, 50))
            # print("dice clicked")
            # dice_number = random.randint(1, 6)
            if dice_number != 6:
                colour_already_moved = False
                current_position = next(all_position_numbers)
                dice_number = random.randint(1, 6)
                dice_number = 6


            else:
                colour_already_moved = False
                dice_number = random.randint(1, 6)
                dice_number = 6
            self.image = pygame.transform.smoothscale(
                pygame.image.load(f'Assets/Dice/D{str(dice_number)}.png').convert_alpha(),
                (50, 50))
            # dice_clicked = True
            # pawn_clicked = False
            # if dice_number == 6:
            #     pass
            # else:








class Pawn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.overlap = False
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
        self.target = []
        self.overlap = False

    def clicked(self):
        global dice_number
        global pawn_clicked
        global dice_clicked
        global colour_already_moved
        # print('dice gamers')
        # if event.type == pygame.MOUSEBUTTONDOWN and dice_clicked is True:
        if event.type == pygame.MOUSEBUTTONDOWN :
            # print(self.number, 'selfnumber,')
            # print(current_position, 'current_position')
            if math.dist((self.path[self.positionNumber][0]+20, self.path[self.positionNumber][1]+20),
                         pygame.mouse.get_pos()) <= 25 and self.number == current_position and pawn_clicked is True and self.target == [] and self.positionNumber + dice_number <= 57 and not colour_already_moved:
                colour_already_moved = True
                # print(self.target)
                # print(self.target.overlap, 'Fuck me!!!!')
                # print(self.target.globalPosition, 'I am dead')
                if self.t == 0 and dice_number == 6:
                    self.t += 1
                elif self.t > 0:
                    self.t += dice_number
                    self.globalPosition += dice_number
                    self.collided = False
                    collision_check(self.color, self)
                # dice_clicked = False
                # pawn_clicked = True

                # if pawn_clicked ==



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
            if self.positionNumber <= 57:
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
        self.image = pygame.image.load('Assets/blue.png')
        self.path = {0: start_position, 1: (780, 0), 2: (0, 0), 3: (100, 300), 4: (100, 100)}
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_position
        self.path = {0: start_position} | path.blue
        self.number = 4
        self.globalPosition = 40

    def home(self):
        """This function is helps to go back to home"""
        self.positionNumber = 0
        self.globalPosition = 40
        self.t = 0


class YellowPawn(Pawn):
    def __init__(self, start_position):
        super().__init__()
        self.color = 'yellow'
        self.image = pygame.image.load('Assets/yellow.png')
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
        self.image = pygame.image.load('Assets/green.png')
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
if no_of_players == 2:
    red1 = RedPawn((60, 59 + 76))
    red2 = RedPawn((60, 138 + 76))
    red4 = RedPawn((140, 138 + 76))
    red3 = RedPawn((140, 59 + 76))

    yellow1 = YellowPawn((500, 495))
    yellow2 = YellowPawn((418, 495))
    yellow3 = YellowPawn((500, 572))
    yellow4 = YellowPawn((418, 572))
    all_sprites.add(red1, red2, red3, red4, yellow1, yellow2, yellow3, yellow4)

    all_position_numbers = itertools.cycle([1, 3])


    def movement_caller():
        red1.movement2()
        red2.movement2()
        red3.movement2()
        red4.movement2()
        yellow1.movement2()
        yellow2.movement2()
        yellow3.movement2()
        yellow4.movement2()

elif no_of_players == 3:
    red1 = RedPawn((60, 59 + 76))
    red2 = RedPawn((60, 138 + 76))
    red4 = RedPawn((140, 138 + 76))
    red3 = RedPawn((140, 59 + 76))

    green1 = GreenPawn((418, 60 + 75))
    green2 = GreenPawn((418, 139 + 75))
    green3 = GreenPawn((500, 60 + 75))
    green4 = GreenPawn((500, 139 + 75))

    yellow1 = YellowPawn((500, 495))
    yellow2 = YellowPawn((418, 495))
    yellow3 = YellowPawn((500, 572))
    yellow4 = YellowPawn((418, 572))
    all_sprites.add(red1, red2, red3, red4, green1, green2, green3, green4, yellow1, yellow2, yellow3, yellow4)
    all_position_numbers = itertools.cycle([1, 2, 3])
    def movement_caller():
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

elif no_of_players == 4:

    red1 = RedPawn((60, 59 + 76))
    red2 = RedPawn((60, 138 + 76))
    red4 = RedPawn((140, 138 + 76))
    red3 = RedPawn((140, 59 + 76))

    green1 = GreenPawn((418, 60 + 75))
    green2 = GreenPawn((418, 139 + 75))
    green3 = GreenPawn((500, 60 + 75))
    green4 = GreenPawn((500, 139 + 75))

    yellow1 = YellowPawn((500, 495))
    yellow2 = YellowPawn((418, 495))
    yellow3 = YellowPawn((500, 572))
    yellow4 = YellowPawn((418, 572))

    blue1 = BluePawn((60, 495))
    blue2 = BluePawn((140, 495))
    blue3 = BluePawn((140, 572))
    blue4 = BluePawn((60, 572))
    all_sprites.add(red1, red2, red3, red4, green1, green2, green3, green4, yellow1, yellow2, yellow3, yellow4, blue1, blue2, blue3, blue4)
    all_position_numbers = itertools.cycle([1, 2, 3])

    def movement_caller():
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
        blue1.movement2()
        blue2.movement2()
        blue3.movement2()
        blue4.movement2()



d = Disc()
dice.add(d)


# print(red.sprites())
# print(green.sprites())
# all_sprites = pygame.sprite.Group()
# print(all_sprites)
# <-----------------------Object Creation--------------->
# def resume():
#     sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#     val = ("John", "Highway 21")
#     mycursor.execute(sql, val)
#     pass






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
    sprites = all_sprites.copy()
    # print(all_sprites)
    sprites.remove(currently_moving)
    # print(sprites)
    # print(sprites)
    # sprites = [red1.globalPosition, red2.globalPosition, red3.globalPosition, red4.globalPosition]
    #
    # # sprite_speed = [red1, red2, red3, green1, green2, green3, green4, yellow1, yellow2, yellow3, yellow4]
    # for i in sprites:
    #
    #
    # try:
    #     sprites.index()
    # sprites = {'red': (red1, red2, red3, red4), 'green': (green1, green2, green3, green4), 'yellow': (yellow1, yellow2)}
    # sprites = [red1, red2, red3, red4, green1, green2, green3, green4]
    # sprites.remove(re)


    # sprites.pop(color)
    collision_targets = sprites

    # list of tuples of different colors
    # print(collision_targets)
    # print(currently_moving.overlap)
    for i in collision_targets:
        if currently_moving.globalPosition == i.globalPosition and currently_moving.color == i.color:
            print('Fuck you')
            # i.overlap = True
            i.overlap = True
            # currently_moving.target.append(i)
            i.target.append(currently_moving)
            print('i am i ',i.number, i.color)
        elif currently_moving.globalPosition != i.globalPosition and currently_moving.color == i.color:
            try:
                i.target.remove(currently_moving)
            except ValueError:
                pass

            # for k in i.target:
            #     print('target for i', k.number, k.color, k.path[0])
            #
            # for j in currently_moving.target:
            #     print('target for currently_moving', j.number, j.color, j.path[0])
            # print(currently_moving.target)
            # currently_moving.overlap = True
            # i.target.append(i)

        elif currently_moving.globalPosition == i.globalPosition and i.globalPosition not in [1, 9, 14, 22, 27, 35, 40, 48]:
            i.home()
        # else:
        #     i.target.remove(currently_moving)
        # else:
        #     currently_moving.overlap = False





def check_for_pawn_click():
    if current_position == 1:
        red1.clicked()
        red2.clicked()
        red3.clicked()
        red4.clicked()
    elif current_position == 2:
        green1.clicked()
        green2.clicked()
        green3.clicked()
        green4.clicked()
    elif current_position == 3:
        yellow1.clicked()
        yellow2.clicked()
        yellow3.clicked()
        yellow4.clicked()
    elif current_position == 4:
        blue1.clicked()
        blue2.clicked()
        blue3.clicked()
        blue4.clicked()

# sprites = {'red': (red1, red2, red3, red4), 'green': (green1, green2, green3, green4), 'yellow':(yellow1,)}
globals = []
# collision_check(sprites)

while carryOn:
    # for k in i.target:
    #     print('target for i', k.number, k.color, k.path[0])
    #
    # for j in currently_moving.target:
    #     print('target for currently_moving', j.number, j.color, j.path[0])
    # print(red1.target[0], 'red1')

    # print(red2.target[0],'red2')
    # print(red2.target[0], 'red3')
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (21, 19, 21), pygame.Rect(0, 0, size[0], 75))
    pygame.draw.rect(screen, (21, 19, 21), pygame.Rect(0, size[1] - 140, size[1], 140))
    screen.blit(board, (0, 75))

    # pygame.draw.circle(screen, (255, 0, 0), (285, 750), 25)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(360, 0, 300, 75), 0, 10)
    pygame.draw.rect(screen, (225, 39, 39), pygame.Rect(-60, 0, 300, 75), 0, 10)
    pygame.draw.rect(screen, (230, 220, 36), pygame.Rect(350, 680, 300, 75), 0, 10)
    pygame.draw.rect(screen, (15, 45, 195), pygame.Rect(-60, 680, 300, 75), 0, 10)
    # red.draw(screen)
    # green.draw(screen)
    screen.blit(pawn1_avatar_image, (25, 20))
    screen.blit(pawn2_avatar_image, (535,20))
    screen.blit(pawn3_avatar_image, (25, 700))
    screen.blit(pawn4_avatar_image, (535, 700))


    textprint(player1, (145,40), (0, 0, 0))
    textprint(player2, (450, 40), (255, 255, 255))
    textprint(player3, (450, 720), (0, 0, 255))
    textprint(player4, (145, 720), (0, 255, 0))
    textprint("Turn", (300, 55), (255, 255, 255))
    if current_position == 1 or current_position == 0:
        textprint("Red's", (300, 25), (255, 255, 255))
    elif current_position == 2:
        textprint("Green's", (300, 25), (255, 255, 255))
    elif current_position == 3:
        textprint("Yellow's", (300, 25), (255, 255, 255))
    elif current_position == 4:
        textprint("Blue's", (300, 25), (255, 255, 255))
    textprint(str(dice_number), (300, 770), (255, 255, 255))
    # print(all_sprites)
    all_sprites.draw(screen)
    dice.draw(screen)

    movement_caller()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_for_pawn_click()
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
            elif event.key == pygame.K_r:
                resume()

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



#line 94

#line 34