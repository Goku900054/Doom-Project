import vizdoom as vzd
import time

game = vzd.DoomGame()

game.load_config(vzd.scenarios_path + "/basic.cfg")
game.set_window_visible(True)

game.init()
game.new_episode()

print("Doom launched successfully!")

time.sleep(5)

game.close()