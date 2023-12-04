import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint
from boom import Boom

class AlienInvasion:
	def __init__(self):
		pygame.init()
		self.settings = Settings() 
		#self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Режим окна
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # Полноэкранный режим
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption(" ---Alien Invasion--- ")
		self.ship = Ship(self)	#создается экземпляр обьекта корабля	
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()
		self._create_fleet()
		self.clock = pygame.time.Clock()
		self.booms = pygame.sprite.Group()
	def run_game(self):
		"""Основной цикл игры"""
		while True:
			self.make_star()
			self._check_events()
			self.ship.update()
			self.bullets.update()
			self._update_aliens()
			self.update_booms()
			self.collision_update()
			self.stars.update()
			self._update_screen()

	def _check_events(self):
		"""Обрабатывает нажатия клавиш и события мыши"""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
					
	def _check_keydown_events(self,event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_RIGHT:
#			print(self.bullets)
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
					
	def _create_fleet(self):
	#создание флота
		alien = Alien(self)
		alien_width = alien.rect.width
		alien_height = alien.rect.width
		
		available_space_x = self.settings.screen_width - (2*alien_width)
		number_aliens_x = available_space_x // (2*alien_width)
		
		available_space_y = self.settings.screen_height - (4*alien_height)
		number_rows = available_space_y // (2*alien_height)
		
		for alien_row in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_row, alien_number)

	def _create_alien(self, alien_row, alien_number):
		alien = Alien(self)
		alien_width = alien.rect.width
		alien_height = alien.rect.height
		alien.x = alien_width + 2*alien_width * alien_number
		alien.rect.x = alien.x
		alien.y = alien_height + 2*alien_height * alien_row
		alien.rect.y =alien.y
		self.aliens.add(alien)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		for star in self.stars.sprites():
			star.draw_star()
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for boom in self.booms.sprites():
			boom.draw_boom()
		self.aliens.draw(self.screen)	
		pygame.display.flip()
		self.clock.tick(self.settings.FPS)	

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def make_star(self):
#Мелькающие звезды. Имитация скорости		
		if randint(0, 15) == 7:
			new_star = Star(self)
			self.stars.add(new_star)

	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self.change_fleet_direction()
				break
	def change_fleet_direction(self):
		#drop all fleet
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1	

	def collision_update(self):
		destroyed_aliens = pygame.sprite.groupcollide(self.bullets, self.aliens,True, True)
		for destroyed_alien in destroyed_aliens:
			x = destroyed_alien.rect.x
			y = destroyed_alien.rect.y
			newboom = Boom(self, destroyed_alien)
			self.booms.add(newboom)	

		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()

	def update_booms(self):
		# удаление 
		for boom in self.booms.copy():
			if boom.flip_count <= 0:
				self.booms.remove(boom)

if __name__=='__main__':
	ai = AlienInvasion()
	ai.run_game()		