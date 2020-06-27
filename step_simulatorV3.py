import pygame

pygame.init()
pygame.font.init()

pi = 3.14159265359
current_steps_left = 0
current_steps_right = 0
running = True
diameter = int(input("Enter the diameter: "))
step_angle = float(input("Enter the step angle: "))
decision = input("Enter forward if you want to move forward or turn of you want to turn: ")
if decision == "forward":
    distance = int(input("Enter the distance: "))
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
    motors = int(input("Enter 1 for a single motor turn or 2 for a double motor turn: "))
    turn_direction = input("Enter which way you want to turn: ")
    width = int(input("Enter the width of the robot: "))
    ratio = 360 / step_angle
    circumference = diameter * pi
    step_distance = circumference / ratio
    if motors == 1:
        distance = width * pi / 2
        if turn_direction == "right":
            direction_left = "forward"
            direction_right = "--"
            change_left = 1
        else:
            direction_left = "--"
            direction_right = "forward"
            change_right = 1

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

left_angle = 0
right_angle = 0
distance_travelled_left = 0
distance_travelled_right = 0
white = (255,255,255)
screen = pygame.display.set_mode((1024,575))

pygame.display.set_caption(("Step Simulator"))
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
    font = pygame.font.Font('freesansbold.ttf', 27)
    text = font.render(write_text, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg = pygame.image.load('background.png')
    bg = pygame.transform.scale(bg, (1024,575))
    screen.blit(bg, (0, 0))
    img  = pygame.image.load("wheel.png")
    img = pygame.transform.scale(img,(200,200))
    if direction_left != "--":
        if steps > current_steps_left:
            current_steps_left += 1
            left_angle += step_angle

    if direction_right != "--":
        if steps > current_steps_right:
            current_steps_right += 1
            right_angle += step_angle

    if direction_left != "--":
        distance_travelled_left = current_steps_left * step_distance * change_left
    if direction_right != "--":
        distance_travelled_right = current_steps_right * step_distance * change_right
    write(direction_left, white, 30, 359)
    write(direction_right, white, 525, 359)
    write(str(current_steps_left), white, 30, 444)
    write(str(current_steps_right), white, 525, 444)
    write(str(distance_travelled_left), white, 30, 529)
    write(str(distance_travelled_right), white, 525, 529)
    rotate(screen, img, (432.5, 152), (100, 100), -left_angle)
    rotate(screen, img, (778.5, 152), (100, 100), -right_angle)
    pygame.display.update()
