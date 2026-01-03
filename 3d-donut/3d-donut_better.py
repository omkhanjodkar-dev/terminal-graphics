import os
import math
import time
# import keyboard

# for i in range(1000):
# 	keyboard.press_and_release("ctrl+-")


cmd = 'cls'

light_ascii = '█▉▊▏▓▒░'
light_ascii = '█▓▒░@%#*+=-:.·'
light_ascii = '█▓▓▒▒░░'
light_ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`.'
light_ascii = '█▓▒░@%#*+=-:. '
light_ascii = '@%#*+=-:.'
light_ascii = '.,-~:;=!*#$@'[-1::-1]

r = 2.7
R = 7

z_max = 0
z_min = 0

x_max = 10
x_min = -10

y_max = 10
y_min = -10


jump = 0.1
div = 10

printables = []

t = 0.1
while t < 2*math.pi and t > 0:
	printable = ''

	z_max = abs((r+1)*math.cos(t))+abs((R+r + 1)*math.sin(t))
	z_min = -z_max
	printable += f'z_max={z_max}\nt≈{int(t)}\n'

	x = x_min + 1
	while x > x_min and x < x_max:
		y = y_max - 1
		while y < y_max and y > y_min:
			lie = ' '
			z = z_max - jump
			while z < z_max and z > z_min:
				if int(int((-x*math.sin(t)+z*math.cos(t))**2+(R-((x*math.cos(t)+z*math.sin(t))**2+y**2)**0.5)**2)/div)==int(int(r**2)/div):
					diff = z_max-z_min
					seglen=diff/len(light_ascii)
					lie = light_ascii[int((z_max-z)/seglen)]
					break
				z -= jump
			# print(lie, end='')
			printable += lie
			y -= 0.5
		# print()
		printable += '\n'
		x += 1
	os.system(cmd)
	t += 0.1

	print(printable)
	printables.append(printable)



input("Waiting for input...")

for i in printables:
	os.system(cmd)
	print(i)
	time.sleep(0.05)