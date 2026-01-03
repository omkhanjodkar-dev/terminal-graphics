import os

light_ascii = '@%#*+=-:.'
light_ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`.'
light_ascii = '█▓▒░@%#*+=-:. '
light_ascii = '█▉▊▏▓▒░'
light_ascii = '█▓▓▒▒░░'
light_ascii = '█▓▒░@%#*+=-:.·'


# for i in range(1):
z_max = 3
z_min = -3

x_max = 10
x_min = -10

y_max = 10
y_min = -10

r = 2.7
R = 7

jump = 0.01
div = 1


x = x_min + 1
while x > x_min and x < x_max:
	y = y_max - 1
	while y < y_max and y > y_min:
		lie = ' '
		z = z_max - jump
		while z < z_max and z > z_min:
			if int(int(z**2+(R-(x**2+y**2)**(1/2))**2)/div) == int(int(r**2)/div):
					diff = z_max-z_min
					seglen=diff/len(light_ascii)
					lie = light_ascii[int((z_max-z)/seglen)]
					break
			z -= jump
		print(lie, end='')
		y -= 0.5
	print()
	x += 1
	# os.system("cls")