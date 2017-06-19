class Settings():
	""" A class tos tore all the settings for Alien Invasion. """

	def __init__(self):
		"""Initialize the game's settings"""

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ships_limit = 3
		
		# Bullet settings
		self.bullet_width = 6
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Alien Settings
		self.fleet_drop_speed = 10	

		#How quicly the game speeds up
		self.speedup_scale = 1.1
		#How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		""" Initialize settings that change throughout the game."""
		self.ship_speed_factor = 3
		self.bullet_speed_factor = 6
		self.alien_speed_factor = 2

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		#Scoring
		self.alien_points = 50 
	def increase_speed(self):
		"""Increase speed settings and alien points """
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)