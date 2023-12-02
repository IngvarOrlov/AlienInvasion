import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.star_color
# прямоугольник строится с нуля. Задатся координата левого верхнего угла, ширина и высота
		self.rect = pygame.Rect(0 ,0, randint(1, 2),randint(2, 3)) 
		self.rect.x = randint(0,self.settings.screen_width)

		self.y = float(self.rect.y)
		self.stars = ai_game.stars
		self.speed = randint(1, 5)
	def update(self):
		self.y += self.speed
		self.rect.y = self.y
		self._update_stars()

	def draw_star(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

	def _update_stars(self):
		# удаление звезд
		for star in self.stars.copy():
			if star.rect.top >= self.settings.screen_height:
				self.stars.remove(star)