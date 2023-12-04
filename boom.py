import pygame
from pygame.sprite import Sprite


class Boom(Sprite):
	def __init__(self, ai_game, alien):
		super().__init__()
		self.flip_count = 40
		self.booms = ai_game.booms
		self.screen = ai_game.screen #экран присваивается атрибуту 
		self.settings = ai_game.settings 
		#self.screen_rect = ai_game.screen.get_rect() #программа обращается к атрибуту rect обьекта экрана при помощи метода get_rect()
		self.image = pygame.image.load('images/boom1.png') 
		self.rect = self.image.get_rect()

		self.rect.midbottom = alien.rect.midbottom
	
	def draw_boom(self):
		if self.flip_count <= 15:
			self.image = pygame.image.load('images/boom2.png')
		if self.flip_count > 0:
			self.screen.blit(self.image, self.rect)
			self.flip_count -= 1
	
	

				