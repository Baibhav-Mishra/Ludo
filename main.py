import pygame
import math
import path
pygame.init()
paused = False
red = pygame.sprite.Group()
green = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
size = (600, 800)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("Ludo")
board = pygame.image.load('Assets/board.png')
pygame.display.set_icon(board)
carryOn = True
clock = pygame.time.Clock()

font = pygame.font.Font('Assets/Montserrat-Regular.ttf', 25)
text = font.render('PAUSE', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (300, 230)

# <-------------Music----------->
pygame.mixer.init()
pygame.mixer.music.load('Assets/Desmeon - Hellcat [NCS Release].mp3')
# pygame.mixer.music.play(0)
# <-------------Music----------->

class Disc:
    def __init__(self):
        self.image = None
class Pawn(pygame.sprite.Sprite):
    def __init__(self, start_position):
        super().__init__()
        self.positionNumber = 1      # changed to 1
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

        # self.blit()

    def movement(self, dice_number):
        if self.positionNumber != dice_number + 1:
            x_complete = y_complete = False
            previous_coordinate = self.path[self.positionNumber - 1]
            # print(previous_coordinate)
            # screen.blit(self.image, (self.path[self.positionNumber]))
            t = self.path[self.positionNumber][0] - previous_coordinate[0]
            z = self.path[self.positionNumber][1] - previous_coordinate[1]
            # print(t,z)
            if self.dx < t:
                self.dx += 1
            elif self.dx > t and t < 0:
                self.dx -= 1
            else:
                x_complete = True

            if self.dy < z:
                self.dy += 1
            elif self.dy > z and z < 0:
                self.dy -= 1
            else:
                y_complete = True
            screen.blit(self.image, (previous_coordinate[0] + self.dx, previous_coordinate[1] + self.dy))
            # print(previous_coordinate[0] + self.dx, previous_coordinate[1] + self.dy)
            if x_complete and y_complete:
                # print(self.positionNumber)
                self.positionNumber += 1
                self.dx = self.dy = 0
                self.inMotion = False
                self.moved = True
        else:
            screen.blit(self.image, (self.path[self.positionNumber - 1]))

    def clicked(self):
        if math.dist((self.path[self.positionNumber - 1]), pygame.mouse.get_pos()) <= 40:
            print('clicked', self.color)

    def check_for_collision(self):
        pass
        # all_sprites.remove(self)

        # for i in collide_check:
        #     print(i)
        # print(collide_check)

    def movement2(self, movement_no):
        if not self.collided:
            # print(self.path[0])
            pygame.draw.rect(screen, (0,0,0), self.rect, 2)
            x_complete = y_complete = False
            # print(t)
            point = self.path[self.positionNumber]
            print(self.positionNumber)
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
                if self.positionNumber != movement_no + 1:
                    self.positionNumber += 1

    def update(self, j):
        global l
        global x
        x_complete = y_complete = False
        self.collided = False
        self.positionNumber = 1
        x = 0
        # print(self.path[0])

        point = self.path[0]
        # print(point[1], self.rect.y)
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
            l.remove(j)
            pass



class RedPawn(Pawn):
    def __init__(self, start_position):

        super().__init__(start_position)
        self.color = 'red'
        self.image = pygame.image.load('Assets/untitled (1).png')
        self.rect = self.image.get_rect()
        self.rect.size = 10, 10
        self.rect.x, self.rect.y = start_position
        self.path = {0: start_position} | path.red | {59: start_position} | {60: (0,0)}
        # self.starPosition = 'a'

    # def star_postion_check(self):
    #     pass
        # if path[self.positionNumber] >= 19 and path[self.positionNumber] <= 34:
        #     self.starPosition = 'b'
        #     pass

        # self.path = {0: start_position} | {2: (0,0)}


class BluePawn(Pawn):
    def __init__(self, start_position):
        super().__init__(start_position)
        self.color = 'blue'
        self.image = pygame.image.load('Assets/untitled (1).png')
        self.path = {0: start_position, 1: (780, 0), 2: (0, 0), 3: (100, 300), 4: (100, 100)}


class YellowPawn(Pawn):
    def __init__(self, start_position):
        super().__init__(start_position)
        self.color = 'yellow'
        self.image = pygame.image.load('Assets/untitled (1).png')
        self.path = {0: start_position, 1: (300, 350), 2: (250, 0), 3: (100, 300), 4: (100, 100)}


class GreenPawn(Pawn):
    def __init__(self, start_position):
        super().__init__(start_position)
        self.color = 'green'
        self.image = pygame.image.load('Assets/untitled (1).png')
        self.rect = self.image.get_rect()
        self.rect.size = 10, 10
        self.rect.x, self.rect.y = start_position
        self.path = {0: start_position} | path.green
        # self.path = {0: (0, 0)}


# <-----------------------Object Creation--------------->
red1 = RedPawn((141,139+76))
red2 = RedPawn((141, 60+76))
red3 = RedPawn((61, 60+76))
red4 = RedPawn((61, 139+76))

# red.add(RedPawn((141, 60+76)))
# red.add(RedPawn((61, 60+76)))
# red.add(RedPawn((61, 139+76)))

green1 = GreenPawn((419, 60+76))
green2 = GreenPawn((419, 139+76))
green3 = GreenPawn((501, 60+76))
green4 = GreenPawn((501, 139+76))

# red.add(red1, red2, red3, red4)
red.add(red2)
green.add(green2, green3, green4, red1, green1)
# all_sprites.add(red1, red2, red3, red4, green1, green2, green3, green4)
# print(all_sprites.sprites())

# print(red.sprites())
# print(green.sprites())
# all_sprites = pygame.sprite.Group()
# print(all_sprites)
# <-----------------------Object Creation--------------->

def button():
    pass
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
    if pygame.mouse.get_pressed(num_buttons=3)[0] and 390 > pygame.mouse.get_pos()[0] > 210 and math.dist((volume_variable, y + 10), pygame.mouse.get_pos()) <= 40:
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
def g(a,d):
    return g(a,d)
l = []
x = 2
while carryOn:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (21, 19, 21), pygame.Rect(0, 0, size[0], 75))
    pygame.draw.rect(screen, (21, 19, 21), pygame.Rect(0, size[1]-100, size[1], 100))

    screen.blit(board, (0, 75))
    pygame.draw.circle(screen, (255, 0, 0), (285, 750), 25)
    pygame.draw.rect(screen, (24, 24, 24), pygame.Rect(360, 0, 300, 75), 0, 10)
    pygame.draw.rect(screen, (24, 24, 24), pygame.Rect(-60, 0, 300, 75), 0, 10)


    # screen.blit(test_spirit, (241, 441 - t))
    # screen.blit(test_spirit, (59.62, 419.84))

    # screen.blit(test_spirit, path_red)
    # p1.blit()
    # p1.first_motion()
    # p2.blit()
    # p2.first_motion()
    # p3.first_motion()
    # red1.movement(46)
    # red1.check_for_collision()
    # p2.movement(0)
    # p3.movement(0)
    # p4.movement(0)
# The world is a good place
#     red.draw(screen)
    green.draw(screen)
    red1.movement2(20)
    green4.movement2(0)

    # red1.movement2(20)
    # red2.movement2(2)
    # green2.movement2(2)
    # green1.movement2(2)
    # green3.movement2(4)
    # green4.movement2(4)
    # red.draw(screen)
    # print(t1.rect)
    # Collidecheck = pygame.sprite.spritecollide(p1, all_sprites, True, pygame.sprite.collide_circle)
    # print(Collidecheck)
    # g1.movement(0)
    # t2.movement(0)
    # t3.movement(0)
    # t4.movement(0)
    # p3.movement(4)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            red1.clicked()
            red2.clicked()


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
