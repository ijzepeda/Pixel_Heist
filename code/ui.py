import pygame

class UI:
	def __init__(self,surface):
		"""This class is used to create the user interface for the game"""
		# setup 
		self.display_surface = surface 

		# health 
		self.health_bar = pygame.image.load('../graphics/ui/health_bar.png').convert_alpha()
		self.health_bar_topleft = (54,39)
		self.bar_max_width = 152
		self.bar_height = 4

		# coins 
		self.coin = pygame.image.load('../graphics/ui/coin.png').convert_alpha()
		self.coin_rect = self.coin.get_rect(topleft = (50,61))

		#Create shadow to numeric font
		self.font = pygame.font.Font('../graphics/ui/Valorax-lg25V.otf',45)
		self.font2 = pygame.font.Font('../graphics/ui/Valorax-lg25V.otf',40)

	def show_health(self,current,full):
		"""This method is used to show the health bar"""

		self.display_surface.blit(self.health_bar,(20,10))
		current_health_ratio = current / full
		current_bar_width = self.bar_max_width * current_health_ratio
		health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
		pygame.draw.rect(self.display_surface,'#FF7B7B',health_bar_rect)

	def show_coins(self,amount):
		"""This method is used to show the coins"""
		
		self.display_surface.blit(self.coin,self.coin_rect)
		coin_amount_surf = self.font.render(str(amount),False, '#C6047E'  ) #xl
		coin_amount_surf2 = self.font2.render(str(amount),False,'#ffc800')  #sm
		coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 2,self.coin_rect.centery))
		self.display_surface.blit(coin_amount_surf,coin_amount_rect)
		self.display_surface.blit(coin_amount_surf2,coin_amount_rect)