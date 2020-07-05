import pygame

pygame.init()
pygame.font.init()
constant = 37.5
pi = 3.14159265359
current_steps_left = 0
current_steps_right = 0
running = True
diameter = int(input("Enter the diameter: "))
step_angle = float(input("Enter the step angle: "))
motors = int(input("Enter 1 for a single motor turn or 2 for a double motor turn: "))
width = int(input("Enter the width of the robot: "))
white = (255,255,255)
k = 10
screen = pygame.display.set_mode((1200,600))
screen.fill((white))
bg = pygame.image.load('background_s.png')
bg = pygame.transform.scale(bg, (600, 600))
screen.blit(bg, (600, 0))
img = pygame.image.load("wheel.png")
img = pygame.transform.scale(img, (120, 120))
pygame.display.set_caption(("Step Simulator"))
pygame.display.update()


maze = [

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

]

maze_2 = [

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

]



maze_wall = [

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', 'C'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',
     '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!'],

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

]
def draw():
    running = True

    maze_2[15][0] = "explored"
    while running:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                running = False
                break
            if event.type == pygame.QUIT:
                running = False


        # Drawing the Red rectangle which signifies the bot.

        pygame.draw.rect(screen, (51, 153, 255), [0 * constant, 15 * constant, constant, constant])

        # Calling the functions which display the walls and the numbers

        wall_detect()

        pygame.display.update()
def show_num(x, y, val):
    font = pygame.font.Font('freesansbold.ttf', 27)
    num = font.render(val, True, (0, 0, 0))
    screen.blit(num, (x, y))

def write(write_text, color , x , y):
    font = pygame.font.Font('freesansbold.ttf', 27)
    text = font.render(write_text, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()


def wall_detect():
    for wall_y in range(32):
        for wall_x in range(31):
            if maze_wall[wall_x][wall_y] == 'w':
                check_b = True
                check_l = True
                check_r = True
                check_t = True
                if wall_y == 0:
                    check_l = False

                if wall_x == 0:
                    check_t = False

                # If there is a cell surrounding the wall on the left, then draw a rectangle which is vertical
                if check_l == True and maze_wall[wall_x][wall_y - 1] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y + 1) / 2 * constant - 2, (wall_x) / 2 * constant, 4, 39])

                # If there is a cell surrounding the wall on the top, then draw a rectangle which is horizontal
                if check_t == True and maze_wall[wall_x - 1][wall_y] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y) / 2 * constant, (wall_x + 1) / 2 * constant - 2, 39, 4])
def num_detect():
    for y in range(16):
        for x in range(16):
            d = maze[x][y]
            show_num(y * constant + k, x * constant + k, str(d))

def complete_revert():
    for y in range(16):

        for x in range(16):
            maze[x][y] = 'e'

def fill(detect):
    check_t = True

    check_r = True

    check_b = True

    check_l = True

    c = 0

    enter = True

    while enter:

        enter = False

        # Checking all the cells in the maze

        for x in range(16):

            for y in range(16):

                if maze[x][y] == c:
                    a = x
                    b = y
                    enter = True
                    check_b = True

                    check_l = True

                    check_r = True

                    check_t = True

                    # Checking whether there is a wall between the cell and its adjecent cells

                    if y == 0 or maze_wall[x * 2][(y * 2) - 1] == 'w':
                        check_l = False

                    if y == 15 or maze_wall[x * 2][(y * 2) + 1] == 'w':
                        check_r = False

                    if x == 0 or maze_wall[(x * 2) - 1][y * 2] == 'w':
                        check_t = False

                    if x == 15 or maze_wall[(x * 2) + 1][y * 2] == 'w':
                        check_b = False

                    # If there is no wall and the cell does not have a number then it assigns the cell with a value of c+1

                    if check_l == True and maze[x][y - 1] == 'e':
                        maze[x][y - 1] = c + 1

                    if check_r == True and maze[x][y + 1] == 'e':
                        maze[x][y + 1] = c + 1

                    if check_t == True and maze[x - 1][y] == 'e':
                        maze[x - 1][y] = c + 1

                    if check_b == True and maze[x + 1][y] == 'e':
                        maze[x + 1][y] = c + 1

        # C is incremented by one so when it finishes all the cells with a value of c, it moves on to the next number that is c+1

        c += 1
    if detect:
        num_detect()


# The click detect function allows the user to enter the walls accordingly into the maze
def click_detect():
    # Infinite Loop
    running = True
    pressed = False
    save = False

    while running:

        check_b = True
        check_l = True
        check_r = True
        check_t = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                if event.key == pygame.K_s:
                    save = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                (x, y) = pygame.mouse.get_pos()
                # Recognises which cell the mouse pointer is in
                x_dist = x % 37.5
                y_dist = y % 37.5
                x_wall = x - x_dist
                y_wall = y - y_dist
                x_wall = int((x_wall / 37.5) * 2)
                y_wall = int((y_wall / 37.5) * 2)

                if x_wall == 0:
                    check_l = False

                if y_wall == 0:
                    check_t = False

                if y_wall == 31:
                    check_b = False

                if check_l == True and x_dist < 7:
                    if maze_wall[y_wall][x_wall - 1] == 'w':
                        maze_wall[y_wall][x_wall - 1] = 'e'
                    else:
                        maze_wall[y_wall][x_wall - 1] = 'w'


                elif x_dist > 45:
                    if maze_wall[y_wall][x_wall + 1] == 'w':
                        maze_wall[y_wall][x_wall + 1] = 'e'
                    else:
                        maze_wall[y_wall][x_wall + 1] = 'w'

                elif check_t == True and y_dist < 25:
                    if maze_wall[y_wall - 1][x_wall] == 'e':
                        maze_wall[y_wall - 1][x_wall] = 'w'
                    else:
                        maze_wall[y_wall - 1][x_wall] = 'w'

                elif check_b == True and y_dist > 32:
                    if maze_wall[y_wall + 1][x_wall] == 'w':
                        maze_wall[y_wall + 1][x_wall] = 'e'
                    else:
                        maze_wall[y_wall + 1][x_wall] = 'w'

        for x in range(16):
            pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))
        for x in range(17):
            pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))
        pygame.display.update()
        wall_detect()


def path_finder(s_row, s_col, final):
    # Defining few variables
    orientation = "top"
    number = 400
    executed = True
    done = True
    stop = False
    if not final:
        for x in range(16):

            for y in range(16):
                if maze[x][y] == 'e':
                    maze_2[x][y] = "explored"

        for x in range(16):

            for y in range(16):

                if maze_2[x][y] == "e":

                    number_2 = maze[x][y]

                    if number_2 < number:
                        number = number_2

        if done:
            for x in range(16):
                if done:
                    for y in range(16):
                        if done:
                            if maze_2[x][y] == "e":
                                if done:
                                    if maze[x][y] == number:
                                        complete_revert()
                                        maze[x][y] = 0
                                        fill(False)

                                        done = False

    while maze[s_row][s_col] != 0:

        a = s_row
        b = s_col
        if executed:


            check_b = True

            check_l = True

            check_r = True

            check_t = True

            turn_direction = ""
            decision = ""

            # Checking whether there is a wall between the adjecent cells

            if s_col == 0 or maze_wall[s_row * 2][s_col * 2 - 1] == 'w':
                check_l = False

            if s_col == 15 or maze_wall[s_row * 2][s_col * 2 + 1] == 'w':
                check_r = False

            if s_row == 0 or maze_wall[s_row * 2 - 1][s_col * 2] == 'w':
                check_t = False

            if s_row == 15 or maze_wall[s_row * 2 + 1][s_col * 2] == 'w':
                check_b = False

            # if there is no wall and the value of the adjecent cell is less than that of the current cell then the bot moves to that cell

            if check_l == True and maze[s_row][s_col - 1] < maze[s_row][s_col]:

                s_col -= 1
                if orientation == "right" or orientation == "left":
                    decision = "forward"
                if orientation == "top":
                    decision = "turn"
                    turn_direction = "left"
                if orientation == "bottom":
                    decision = "turn"
                    turn_direction ="right"
                orientation = "left"





            elif check_r == True and maze[s_row][s_col + 1] < maze[s_row][s_col]:

                s_col += 1
                if orientation == "right" or orientation == "left":
                    decision = "forward"
                if orientation == "top":
                    decision = "turn"
                    turn_direction = "right"
                if orientation == "bottom":
                    decision = "turn"
                    turn_direction ="left"
                orientation = "right"




            elif check_t == True and maze[s_row - 1][s_col] < maze[s_row][s_col]:

                s_row -= 1
                if orientation == "top" or orientation == "bottom":
                    decision = "forward"
                if orientation == "left":
                    decision = "turn"
                    turn_direction = "right"
                if orientation == "right":
                    decision = "turn"
                    turn_direction ="left"
                orientation = "top"



            elif check_b == True and maze[s_row + 1][s_col] < maze[s_row][s_col]:

                s_row += 1
                if orientation == "top" or orientation == "bottom":
                    decision = "forward"
                if orientation == "right":
                    decision = "turn"
                    turn_direction = "right"
                if orientation == "left":
                    decision = "turn"
                    turn_direction ="left"
                orientation = "bottom"


            a = s_row
            b = s_col
            maze_2[a][b] = "explored"
            print(decision)
            steps, direction_left, direction_right, change_left, change_right, step_distance = simulate(decision,turn_direction , False)

            left_angle = 0
            right_angle = 0
            distance_travelled_left = 0
            distance_travelled_right = 0
            current_steps_right = 0
            current_steps_left = 0
            g = False
            # Infinite Loop

        running = True
        run_rotate = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    running = False

                if event.type == pygame.QUIT:
                    maze[s_row][s_col] = 0
                    running = False
                if not final:
                    screen.fill((255, 255, 255))

                # Drawing the Red rectangle which signifies the bot.
                for x in range(16):

                    for y in range(16):
                        if maze_2[x][y] == "explored":
                            pygame.draw.rect(screen, (102, 255, 178), [y * constant, x * constant, constant, constant])

                pygame.draw.rect(screen, (51, 153, 255), [b * constant, a * constant, constant, constant])

                for x in range(16):
                    pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))

                for x in range(16):
                    pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))
                # Calling the functions which display the walls and the numbers

                wall_detect()
                g = False
                running = start( steps, direction_left, direction_right, change_left, change_right, step_distance , s_row, s_col)
                if decision == "turn":
                    decision = "forward"

                    steps, direction_left, direction_right, change_left, change_right, step_distance = simulate(decision, turn_direction, True)
                    running = start( steps, direction_left, direction_right, change_left, change_right, step_distance , s_row, s_col)







def simulate(decision  , turn_direction ,g):


    if g == True and motors == 1:
        distance = 18 - width/2
    else:
        distance = 18
    if decision == "forward":

        ratio = 360 / step_angle
        circumference = diameter * pi
        step_distance = circumference / ratio
        steps = distance / step_distance

        if distance > 0:
            direction_left = "forward"
            change_right = 1
            change_left = 1
            direction_right = "forward"

        else:
            direction_left = "backward"
            change_right = -1
            direction_right = "backward"
            change_left = -1
            steps = distance / step_distance * -1

    else:

        ratio = 360 / step_angle
        circumference = diameter * pi
        step_distance = circumference / ratio
        if motors == 1:
            distance = width * pi / 2
            if turn_direction == "right":
                direction_left = "forward"
                direction_right = "--"
                change_left = 1
                change_right = 0

            else:
                direction_left = "--"
                direction_right = "forward"
                change_right = 1
                change_left = 0
        else:
            distance = width * pi / 4

            if turn_direction == "right":
                direction_left = "forward"
                change_left = 1

                direction_right = "backward"
                change_right = -1


            else:
                direction_left = "backward"
                change_left = -1

                direction_right = "forward"
                change_right = 1

        steps = distance / step_distance

    return steps , direction_left,direction_right , change_left,change_right , step_distance

def rotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

def write(write_text, color , x , y):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(write_text, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()

def start( steps, direction_left, direction_right, change_left, change_right, step_distance , s_row, s_col):
    left_angle = 0
    right_angle = 0
    distance_travelled_left = 0
    distance_travelled_right = 0
    current_steps_right = 0
    current_steps_left = 0
    run_rotate = True
    g = False
    running = True
    while run_rotate:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                run_rotate = False
                running = False
                return running;

            if event.type == pygame.QUIT:
                maze[s_row][s_col] = 0
                run_rotate = False
                running = False
                return running;
        if direction_left != "--":
            if steps > current_steps_left:
                current_steps_left += 1
                left_angle += step_angle
            else:
                g = True
                run_rotate = False

        if direction_right != "--":
            if steps > current_steps_right:
                current_steps_right += 1
                right_angle += step_angle
            else:
                g = True
                run_rotate = False
        screen.blit(bg, (600, 0))
        if direction_left != "--":
            distance_travelled_left = current_steps_left * step_distance * change_left
        if direction_right != "--":
            distance_travelled_right = current_steps_right * step_distance * change_right
        write(direction_left, white, 625, 374)
        write(direction_right, white, 960, 374)
        write(str(current_steps_left), white, 625, 457)
        write(str(current_steps_right), white, 960, 452)
        write(str(distance_travelled_left), white, 625, 549)
        write(str(distance_travelled_right), white, 960, 549)
        rotate(screen, img, (872, 115), (60, 60), -left_angle)
        rotate(screen, img, (1095, 115), (60, 60), -right_angle)
        pygame.display.update()

click_detect()
draw()
maze[8][7] = 0
maze_2[15][0] = "explored"
fill(False)
path_finder(15,0,True)


