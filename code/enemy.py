import pygame 
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
	"""This class will control enemy movement. Basically loads the images for wlaking, and set transform from left to right until hit a collider of constraints"""
	def __init__(self,size,x,y):	
		super().__init__(size,x,y,'../graphics/enemy/run')
		self.rect.y += size - self.image.get_size()[1]
		self.speed = randint(3,5)

	def move(self):
		self.rect.x += self.speed

	def reverse_image(self):
		if self.speed > 0:
			self.image = pygame.transform.flip(self.image,True,False)

	def reverse(self):
		self.speed *= -1

	def update(self,shift):
		self.rect.x += shift
		self.animate()
		self.move()
		self.reverse_image()