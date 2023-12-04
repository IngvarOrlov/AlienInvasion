from random import randint

class Settings():
	def __init__(self):
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (30, 30, 30)
		self.FPS = 150
		self.ship_speed = 1.3

		self.bullet_speed = 3.5
		self.bullet_width = 7
		self.bullet_height = 11
		self.bullet_color = (170, 20 ,40)
		self.bullets_allowed = 5

		self.star_color = (200,200,100)

		self.alien_speed = 0.5
		self.fleet_drop_speed = 10
		self.fleet_direction = 1 #1:right -1:left