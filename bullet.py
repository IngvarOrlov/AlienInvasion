import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
# прямоугольник строится с нуля. Задатся координата левого верхнего угла, ширина и высота
		self.rect = pygame.Rect(0 ,0, self.settings.bullet_width, self.settings.bullet_height) 
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)
		self.bullets = ai_game.bullets
	def update(self):
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y
		self._update_bullets()

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

	def _update_bullets(self):
		# удаление снарядов
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)