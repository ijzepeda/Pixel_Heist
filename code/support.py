from csv import reader
from settings import tile_size
from os import walk
import pygame

def import_folder(path):
	
	"""Import the folder from the path, and see all items on it. try to avoid DS_Store, that is created on mac"""
	surface_list = []
	"""TODO: For some reason after changing paths, wont load items from the path"""
	for _,__,image_files in walk(path):
		for image in image_files:
			if(image != '.DS_Store'):
				full_path = path + '/' + image
				image_surf = pygame.image.load(full_path).convert_alpha()
				surface_list.append(image_surf)

	return surface_list

def import_csv_layout(path):
	"""Import the csv file, and create a list of lists, with the values of the csv file"""
	terrain_map = []
	with open(path) as map:
		level = reader(map,delimiter = ',')
		for row in level:
			terrain_map.append(list(row))
		return terrain_map

def import_cut_graphics(path):
	"""Import the graphics, and cut them into tiles"""
	surface = pygame.image.load(path).convert_alpha()
	tile_num_x = int(surface.get_size()[0] / tile_size)
	tile_num_y = int(surface.get_size()[1] / tile_size)

	cut_tiles = []
	for row in range(tile_num_y):
		for col in range(tile_num_x):
			x = col * tile_size
			y = row * tile_size
			new_surf = pygame.Surface((tile_size,tile_size),flags = pygame.SRCALPHA)
			new_surf.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size))
			cut_tiles.append(new_surf)

	return cut_tiles
