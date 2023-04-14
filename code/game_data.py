# Make sure that only the first level is activated for 'unlock=1' so when the game reboots to 0's the vector wont get any error
# It happens when the user dies, and tries to create a vector, because 2 levels have been unlocked, but, overworld only will display the first level/Node

level_0 = {
		'terrain': '../levels/0/level_0_terrain.csv',
		# 'bg':'../levels/0/level_0_bg.csv',
		'bg':'../levels/0/level_0_bg.csv', #tiene las cosas en su lugar, pero la imagen esta mal
		'bg1':'../levels/0/level_0_bg.csv', #tiene las cosas en su lugar, pero la imagen esta mal
        
		'coins':'../levels/0/level_0_coins.csv',
		'fg objects':'../levels/0/level_0_fg_objects.csv',
		'bg objects':'../levels/0/level_0_bgObjects.csv',
 		'enemies':'../levels/0/level_0_enemy.csv',
		'constraints':'../levels/0/level_0_constraints.csv',
		'player': '../levels/0/level_0_player.csv',
		'node_pos': (150,260),
		'unlock': 1,
        'vertical_tile_number':20,
        'night':False,
		'node_graphics': '../graphics/overworld/0'}

level_1 = {
		'terrain': '../levels/0/level_0_terrain.csv',
		'bg':'../levels/0/level_0_bg.csv',
        'bg1':'../levels/0/level_0_bg.csv', #tiene las cosas en su lugar, pero la imagen esta mal
        
		'coins':'../levels/0/level_0_coins.csv',
		'fg objects':'../levels/0/level_0_fg_objects.csv',
		'bg objects':'../levels/0/level_0_bgObjects.csv',
 		'enemies':'../levels/0/level_0_enemy.csv',
		'constraints':'../levels/0/level_0_constraints.csv',
		'player': '../levels/0/level_0_player.csv',
		'node_pos': (360,500),
		'unlock': 2,
        'night':True,
        'vertical_tile_number':20,
		'node_graphics': '../graphics/overworld/1'}
     
level_2 = {
		'bg':'../levels/2/level_2_terrain.csv',
		'terrain': '../levels/2/level_2_terrain.csv',
		'coins':'../levels/2/level_2_coins.csv',
		'fg objects':'../levels/2/level_2_fg_objects.csv',
		'bg objects':'../levels/2/level_2_bg_objects.csv',
		'enemies':'../levels/2/level_2_enemies.csv',
		'constraints':'../levels/2/level_2_constraints.csv',
		'player': '../levels/2/level_2_player.csv',
		'node_pos': (650,400),
		'node_graphics': '../graphics/overworld/2',
        'vertical_tile_number':25,
        'night':False,
		'unlock': 3}
level_3 = {
		'bg':'../levels/3/level_3_bg_terrain.csv',
		'terrain': '../levels/3/level_3_terrain.csv',
		'coins':'../levels/3/level_3_coins.csv',
		'fg objects':'../levels/3/level_3_fg_objects.csv',
		'bg terain':'../levels/3/level_3_bg_terrain.csv',
		'bg objects':'../levels/3/level_3_bg_objects.csv',
		'enemies':'../levels/3/level_3_enemies.csv',
		'constraints':'../levels/3/level_3_constraints.csv',
		'player': '../levels/3/level_3_player.csv',
		'node_pos': (820,200),
		'node_graphics': '../graphics/overworld/3',
        'vertical_tile_number':25,
        'night':False,
		'unlock': 4}



levels = {
	0: level_0,
	1: level_1, 
	2: level_2,
	3: level_3  
    }