import pygame

pygame.init()
pygame.font.init()


running = True

diameter = int(input("Enter the diameter: "))
step_angle = float(input("Enter the step angle: "))
pi = 3.14159265359
distance = int(input("Enter the distance: "))

ratio = 360/step_angle

circumference = diameter * pi
step_distance =  circumference/ratio
steps = distance/step_distance
if distance > 0 :
    direction = "forward"
else:
    direction = "backward"
left_angle = 0
right_angle = 0
current_steps = 0
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
    screen.blit(bg, (0, 0))
    img  = pygame.image.load("wheel.png")
    img = pygame.transform.scale(img,(200,200))

    if current_steps < steps:
        current_steps += 1
        left_angle -= 1
        right_angle -= 1
    distance_travelled = current_steps * step_distance
    write(direction, white, 30, 359)
    write(direction, white, 525, 359)
    write(str(current_steps), white, 30, 444)
    write(str(current_steps), white, 525, 444)
    write(str(distance_travelled), white, 30, 529)
    write(str(distance_travelled), white, 525, 529)
    rotate(screen, img, (432.5, 152), (100, 100), left_angle)
    rotate(screen, img, (778.5, 152), (100, 100), right_angle)
    pygame.display.update()
