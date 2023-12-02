import pygame
class Ship():
	def __init__(self,ai_game):
		self.screen = ai_game.screen #экран присваивается атрибуту Ship
		self.settings = ai_game.settings #создается атрибут дляиспользования в update
		self.screen_rect = ai_game.screen.get_rect() #программа обращается к атрибуту rect обьекта экрана при помощи метода get_rect()
		self.image = pygame.image.load('images/ship.png') # метод pygame.image.load() возвращает поверхность представляющую корабль которая присваивается self.image
		self.rect = self.image.get_rect() #программа вызывает get_reсt() для получения атрибута rect поверхности корабля
		self.rect.midbottom = self.screen_rect.midbottom #задаетсятекущая позиция прямоугольника корабля
		self.x =float(self.rect.x) #сохранение вещественной координаты корабля
		#Флаги перемещения
		self.moving_right = False
		self.moving_left = False
	def update(self):
			# движение корабля влево-право в зависимости от положения переключателей
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed

		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x
			
			# изменение спрайта корабля при движении
		if 	self.moving_right and self.moving_left:
			self.image = pygame.image.load('images/ship.png')
		elif self.moving_left:
			self.image = pygame.image.load('images/ship_left.png')
		elif self.moving_right:
			self.image = pygame.image.load('images/ship_right.png')
		else:
			self.image = pygame.image.load('images/ship.png')
	
	def blitme(self):
		self.screen.blit(self.image, self.rect) #рисует корабль в текущей позиции
		

#print (ai.settings.bg_color)		