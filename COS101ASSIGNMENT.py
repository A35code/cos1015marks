def math_and_physics_operations_option():
    print('\nMaths and physics operations option:')
    print('a. Area of Triangle')
    print('b. Pressure of a body')
    print('c. density of a body')
    print('d. sum of interior angles in polygon')
    print('e. acceleration of a body')
    print('f. ending ')

math_and_physics_operations_option()

options = input('pick an option from a to f  ')
print(options)

if options == 'a':
    breath = int(input('Enter breath of triangle  '))
    height = int(input('enter height of triangle  '))
    area = 0.5 * breath * height
    print(' area of triangle =')
    print(area)

elif options == 'b':
    force = int(input('Enter number  '))
    area = int(input('Enter number  '))
    pressure = force / area
    print(' pressure =')
    print(pressure)

elif options == 'c':
    mass = int(input('Enter number  '))
    volume = int(input('Enter number  '))
    density = mass / volume
    print('density =')
    print(density)

elif options == 'd':
    n = int(input('Enter number of sides of polygon  '))
    sum_of_interior_angles = ( n - 2) * 180
    print(' sum of interior angles =')
    print(sum_of_interior_angles)

elif options == 'e':
    velocity = float(input('Enter value for velocity  '))
    time = int(input('Enter value for time  '))
    acceleration = velocity / time
    print(' acceleration =')
    print(acceleration)

elif options == 'f':
    close = 'THANK YOU FOR YOUR PATRONAGE  '
    matric = 'BHU/24/04/05/0107  '
    name = 'AKWADA EMMANUEL  '
    end = close + matric + name
    print(end)

else :
    print('ERROR FOUND IN THE OPTION WRITTEN PLEASE CHOOSE AN OPTION FROM a TO f')