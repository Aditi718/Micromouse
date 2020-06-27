diameter = int(input("Enter the diameter: "))
step_angle = int(input("Enter the step angle: "))
pi = 3.14159265359
distance = int(input("Enter the distance: "))

ratio = 360/step_angle

circumference = diameter * pi
step_distance =  circumference/ratio
steps = distance/step_distance

print("The number of steps will be " + str(steps))