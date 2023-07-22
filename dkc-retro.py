import retro
import numpy as np
import cv2
import neat
import pickle
import os

env = retro.make('DonkeyKongCountry-Snes', '1Player.CongoJungle.RopeyRampage.Level2')

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, os.path.join(os.path.dirname(__file__), "config_feedforward.txt"))

env.reset()

done = False

while not done:
    env.render()
    action = env.action_space.sample()
    print(action)
    #print(env.get_action_meaning(action))
    ob, rew, done, info = env.step(action)
