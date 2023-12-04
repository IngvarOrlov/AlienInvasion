import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.image = pygame.image.load("images/alien.png")
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.image_position = 1
		self.image_flip = randint(0, 50)
	def update(self):
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x
		#image change
		self.image_flip -=1
		if self.image_flip <=0:
			self.image_flip =25
			self.image_position *= -1
			if self.image_position == -1:
				self.image = pygame.image.load("images/alien.png")
			elif self.image_position == 1:
				self.image = pygame.image.load("images/alien2.png")

	def check_edges(self):
	#return True if alien near screen edge
		screen_rect = self.screen.get_rect()	
		if self.rect.right >= screen_rect.right or self.rect.left <=0:
			return True