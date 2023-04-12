"""
AML1214
Final Assignment
Group mambers:
Ivan Zepeda
Nivedini
Preet
Suzanne
??????

The game has been made using pygame, 
and sprites from craftpix.com
and following pygame documentation, tutorials, and many chunks of code from stackoverflow, chatgpt, youtube and random tutorials

"""

import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI

class Game:
	def __init__(self): 
		"""This class is used to create the game"""
		# game attributes
		self.max_level = 2
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0

		# overworld creation
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'

		# user interface 
		self.ui = UI(screen)

	def create_level(self,current_level):
		""" Create level """
		self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
		self.status = 'level'

	def create_overworld(self,current_level,new_max_level):
		""" Verify unlocked levels, and recreate level_selection"""
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'

	def change_coins(self,amount):
		""" increase the amount of coins"""

		self.coins += amount

	def change_health(self,amount):
		"""Change the health value"""
		self.cur_health += amount

	def check_game_over(self):
		"""Check if the player is dead. if so, set coins to 0, and current level 0"""
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = 'overworld'

	def run(self):
		"""Run the game"""
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('blue')
	game.run()

	pygame.display.update()
	clock.tick(60)