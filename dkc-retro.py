import retro
import numpy as np
import cv2
import neat
import pickle

env = retro.make('DonkeyKongCountry-Snes', '1Player.CongoJungle.RopeyRampage.Level2')

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward')

env.reset()

done = False

while not done:
    env.render()
    action = env.action_space.sample()
    ob, rew, done, info = env.step(action)
