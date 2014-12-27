from PyGlow import PyGlow
from time import sleep
from random import randint

pyglow = PyGlow()

lit = 75
fast = 1000
white = (6, 12, 18)
green = (4, 10, 16)
red = (1, 7, 13)
lights = zip(white, green, red)

def single(color):
	pyglow.set_leds(color, brightness=lit, speed=fast, pulse=True)
	pyglow.update_leds()
	sleep(0.25)

def three():
	if i == 3:
		j = randint(0, 2)		
		pyglow.set_leds(lights[j], brightness=lit, speed=fast, pulse=True)
	else:
		pyglow.set_leds(lights[i], brightness=lit, speed=fast, pulse=True)

	pyglow.update_leds()
	sleep(0.25)




try:
	while True:
		i = randint(0, 3)
		if i == 0:
			single(red)
		elif i == 1:
			single(white)
		elif i == 2:
			single(green)
		elif i == 3:
			three()


except KeyboardInterrupt:
	pyglow.all(0)	
