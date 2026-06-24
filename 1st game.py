import arcade

window = arcade.Window(width=1350,height=687,title="Snake game")
window.center_window()

start_color = (255,255,255,95)

class GameView(arcade.View):
	def __init__(self):
		super().__init__()
		
		self.center_x = 675
		self.center_y = 343
		self.width = 30
		self.height = 30
		self.speed_x = 0
		self.speed_y = 0
		self.color = arcade.color.GREEN
		self.angle = 0
		self.speed = 300
		self.game_over = False
		
		
	def on_draw(self):
		self.clear()
		
		square = arcade.draw_rectangle_filled(
		self.center_x,
		self.center_y, 
		self.width, 
		self.height,
		color = self.color,
		tilt_angle = self.angle,
		)
		
		if self.game_over:
			self.clear()
			arcade.draw_text(
				"GAME OVER",
				start_x=675,
				start_y=343,
				color=arcade.color.RED,
				font_size=50,
				anchor_x="center",
				anchor_y="center"
        )
		
	def on_key_press(self, key, modifiers):
		if key == arcade.key.LEFT:
			self.angle += 90
			self.speed_x = -self.speed
			self.speed_y = 0
			
			
		elif key == arcade.key.RIGHT:
			self.angle -= 90
			self.speed_x = self.speed
			self.speed_y = 0
			
		elif key == arcade.key.UP:
			self.angle = 0
			self.speed_x = 0
			self.speed_y = self.speed

		elif key == arcade.key.DOWN:
			self.angle += 180
			self.speed_x = 0
			self.speed_y = -self.speed

	
	def on_update(self, delta_time:float):
		if not self.game_over:
			self.center_x += self.speed_x*delta_time
			self.center_y += self.speed_y*delta_time
		
			if self.center_x >= 1350 - self.width/2:
				self.game_over = True
		
			elif self.center_x <= self.width/2:
				self.game_over = True
		
			elif self.center_y >= 687 - self.height/2:
				self.game_over = True
		
			elif self.center_y <= self.height/2:
				self.game_over = True
		
	
	
game = GameView()
window.show_view(game)
arcade.run()