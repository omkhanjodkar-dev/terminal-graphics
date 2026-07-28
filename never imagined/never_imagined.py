import time
print("\033[2J\033[H")

ymax = 25
xmax = 50
zmax = 25
xfactor = 1/2

posx = 0
posy = 0
posz = 1
rmax = 2
# rmin = 2

g = 9.8
vx = 5
vy = -5
vz = 5
u = -1

tfactor = 2

prev = time.time()
while True:
	# game loop
	# math
	t = (time.time() - prev) * tfactor
	prev = time.time()

	r = 1 + rmax*(zmax - abs(posz))/zmax
	# r = rmax/posz

	vy += g*t
	posy += vy*t + 0.5*g*t*t
	posx += vx*t
	posz += vz*t

	additivey = ymax/2 * abs(posz)/zmax
	additivex = xmax/4 * abs(posz)/zmax
	if posy > ymax - r - additivey:
		posy = ymax - r - additivey
		vy *= u
	if posy < -ymax+r + additivey:
		posy = -ymax+r + additivey
		vy *= u
	if posx > xmax/2 - r - additivex:
		posx = xmax/2 - r - additivex
		vx *= u
	if posx < -xmax/2 + r + additivex:
		posx = -xmax/2 + r + additivex
		vx *= u
	if posz < 0 + r:
		posz = 0 + r
		vz *= u
	if posz > zmax - r:
		posz = zmax - r
		vz *= u

	# render
	buffer = ''
	for y in range(-ymax, ymax+1):
		for _x in range(-xmax, xmax+1):
			x = _x*xfactor
			if abs(x) == xmax*xfactor:
				char = "|"
			elif abs(y) == ymax:
				char = "_"
			elif (x-posx)**2+(y-posy)**2 <= r**2:
				char = "*"
			elif x==y and (x < -xmax/2+xmax/4 or x > xmax/2 - xmax/4):
				char = "\\"
			elif x==-y and (x < -xmax/2+xmax/4 or x > xmax/2 - xmax/4):
				char = "/"
			elif x == int(-xmax/2+xmax/4) and y < ymax/2 and y > -ymax/2:
				char = "|"
			elif x == int(xmax/2-xmax/4) and y < ymax/2 and y > -ymax/2:
				char = "|"
			elif y == int(ymax-ymax/2) and x < xmax/4 and x > -xmax/4:
				char = "_"
			elif y == int(-ymax+ymax/2) and x < xmax/4 and x > -xmax/4:
				char = "_"
			else:
				char = " "
			buffer += char
		buffer += "\n"
	print("\033[H")
	print(buffer)